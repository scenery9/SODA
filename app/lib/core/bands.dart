/// Severity bands.
///
/// These thresholds are the ones in `api/engine/load.py` and in section 5 of
/// the README. They are duplicated here because the client has to label a
/// cached figure while offline, and nowhere else. If they ever disagree, the
/// server is right: the client never computes a fresh number.
library;

enum Band { light, manageable, heavy, overload }

extension BandLabel on Band {
  /// The word shown beside the number. Severity is never carried by colour
  /// alone, so this string is not optional.
  String get label => switch (this) {
        Band.light => 'Light',
        Band.manageable => 'Manageable',
        Band.heavy => 'Heavy',
        Band.overload => 'Overload',
      };
}

/// Classify on the unrounded score, so 89.6% is Heavy and displays as 90%
/// rather than being promoted by the rounding.
Band bandOf(double percentage) {
  if (percentage >= 90) return Band.overload;
  if (percentage >= 70) return Band.heavy;
  if (percentage >= 50) return Band.manageable;
  return Band.light;
}

/// What a screen reader should hear for a capacity figure.
String capacitySemantics(double percentage) =>
    '${percentage.round()} percent, ${bandOf(percentage).label}';
