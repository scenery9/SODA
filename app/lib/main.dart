/// SODA.
///
/// The app draws and explains; it does not decide. Every capacity figure on
/// screen came from `api/engine/`, and the client never recomputes one. When
/// the network is gone it shows the last figure it was given, with the time it
/// was given, rather than a guess.
library;

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

void main() => runApp(const ProviderScope(child: SodaApp()));

class SodaApp extends StatelessWidget {
  const SodaApp({super.key});

  @override
  Widget build(BuildContext context) => MaterialApp(
        title: 'SODA',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          colorSchemeSeed: const Color(0xFF0E7A5E),
          brightness: Brightness.light,
          useMaterial3: true,
        ),
        darkTheme: ThemeData(
          colorSchemeSeed: const Color(0xFF2FD69C),
          brightness: Brightness.dark,
          useMaterial3: true,
        ),
        // Every screen is drawn for both, rather than one filtered into the
        // other, so accents stay legible in each.
        themeMode: ThemeMode.system,
        home: const Placeholder(),
      );
}
