"""The structural rule, enforced.

BUILD.md calls this the single most important rule in the repository: the
engine makes no network calls and imports nothing from the language layer.
That is what makes "deterministic core" a fact rather than an intention, so
it is checked here instead of being trusted.
"""

import ast
import sys
from pathlib import Path

ENGINE = Path(__file__).resolve().parents[1] / "engine"

#: Anything that could reach the network, a clock, or a random source. A model
#: that quietly depends on the time of day is not reproducible.
FORBIDDEN_MODULES = {
    "requests", "httpx", "urllib", "urllib3", "socket", "http",
    "aiohttp", "openai", "google", "ollama", "random", "secrets",
}
FORBIDDEN_PREFIXES = ("language", "routers", "supabase", "fastapi")


def engine_files():
    return sorted(ENGINE.glob("*.py"))


def imported_names(path: Path):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                yield alias.name
        elif isinstance(node, ast.ImportFrom):
            yield node.module or ""


def test_the_engine_has_files_to_check():
    assert engine_files(), "no engine modules found; the check would pass vacuously"


def test_the_engine_imports_nothing_that_can_reach_the_network():
    offenders = []
    for path in engine_files():
        for name in imported_names(path):
            root = name.split(".")[0]
            if root in FORBIDDEN_MODULES:
                offenders.append(f"{path.name} imports {name}")
    assert not offenders, offenders


def test_the_engine_does_not_import_the_language_layer_or_the_web_layer():
    offenders = []
    for path in engine_files():
        for name in imported_names(path):
            if name.startswith(FORBIDDEN_PREFIXES):
                offenders.append(f"{path.name} imports {name}")
    assert not offenders, offenders


def test_the_engine_never_reads_the_clock_for_a_load_figure():
    """Recovery takes the date as an argument. Nothing else asks what time it
    is, because the same inputs must always give the same number."""
    offenders = []
    for path in engine_files():
        if path.name == "recovery.py":
            continue  # takes `today` as a parameter; never calls date.today()
        source = path.read_text(encoding="utf-8")
        for call in ("datetime.now", "date.today", "time.time"):
            if call in source:
                offenders.append(f"{path.name} calls {call}")
    assert not offenders, offenders


def test_recovery_takes_today_as_an_argument_rather_than_asking():
    source = (ENGINE / "recovery.py").read_text(encoding="utf-8")
    assert "date.today()" not in source
    assert "today: date" in source
