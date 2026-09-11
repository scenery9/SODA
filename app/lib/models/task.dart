/// A commitment.
///
/// `effort` feeds the load calculation. `priority` never does: it only orders
/// what Smart Rebalance is allowed to move. Keeping them apart is what stops a
/// student from lowering their own workload figure by marking things important.
library;

enum Effort { low, medium, high, veryHigh, extraHigh }

enum Priority { low, medium, high }

enum Category { academic, work, social, errands, other }

class Task {
  const Task({
    required this.id,
    required this.title,
    required this.startsAt,
    required this.durationMinutes,
    this.effort = Effort.medium,
    this.priority = Priority.medium,
    this.category = Category.academic,
    this.isFixed = false,
    this.deadlineAt,
  });

  final String id;
  final String title;
  final DateTime startsAt;
  final int durationMinutes;
  final Effort effort;
  final Priority priority;
  final Category category;

  /// Classes and paid shifts. Never offered as something to move.
  final bool isFixed;

  /// Rebalance may not propose anything that crosses this.
  final DateTime? deadlineAt;

  Duration get duration => Duration(minutes: durationMinutes);
}
