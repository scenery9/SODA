"""The deterministic core.

Nothing in this package makes a network call, reads a clock for a load figure,
or imports the language layer. That separation is what makes the arithmetic in
section 5 of the README reproducible, and api/tests/test_engine_is_isolated.py
fails the build if it is ever broken.
"""
