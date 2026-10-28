# Q-Learning in Tic-Tac-Toe – Schülerprojekt

In diesem Projekt programmierst du die zentralen Lernschritte eines Q-Learning-Agenten selbst: die ε-greedy-Aktionswahl und die Q-Update-Regel. Hilfsmethoden sind in `QLearningAgent.py` vorbereitet. Die Trainingsmethode setzt du aus drei Codebausteinen im Arbeitsheft zusammen.

## Spiel- und Lernmodell

- Tic-Tac-Toe auf einem 3×3-Brett.
- Der lernende Agent spielt immer **O**.
- Der Gegner spielt **X**, zieht in jeder Trainingspartie zuerst und wählt danach zufällig unter den freien Feldern.
- Eine Aktion ist ein Feld mit der Nummer `0` bis `8`; es gilt `aktion = zeile * 3 + spalte`.
- Die Q-Tabelle ordnet einem Brettzustand neun Aktionswerte zu.
- Belohnungen: Sieg des Agenten `+1`, Niederlage `-1`, Remis `0`.
- Für die zentrale Implementierung brauchst du nur Python-Standardbibliothek (`random`, `copy`). NumPy ist zunächst nicht nötig.

## Dateien

- `Game.py`: vorgegebene Umgebung; lies insbesondere Brettdarstellung, Zugprüfung, Sieg- und Remisprüfung.
- `QLearningAgent.py`: reduziertes Startergerüst. `choose_action` (TODO A) und `update_q_table` (TODO B) programmierst du. `train_agent` (TODO C) überträgst du vollständig aus den drei aufeinanderfolgenden Codebausteinen im Arbeitsheft. Ersetze nach jedem Auftrag die jeweilige `raise NotImplementedError(...)`-Platzhalterzeile.
- `play_rl_game.py`: trainiert den vervollständigten Agenten, gibt Sieg-/Niederlagen-/Remisquoten je 500 Episoden aus und spielt danach mit epsilon = 0 (greedy) gegen dich.
- `Tic_Tac_Toe_RL_Agent_legacy.ipynb`: unverändertes Notebook aus dem ursprünglichen Repository; es ist archiviert und nicht Teil des aktuellen Arbeitswegs. Es wird später neu besprochen.

## Start

Benötigt wird Python 3.10 oder neuer. Es sind keine zusätzlichen Pakete nötig.

```bash
python --version
python play_rl_game.py
```

`play_rl_game.py` lässt den Agenten standardmässig 20'000 Partien trainieren. Starte erst, nachdem du TODO A und TODO B ergänzt sowie TODO C aus dem Arbeitsheft übertragen hast. Die Hilfsmethoden kannst du vorher einzeln anhand der Prüffälle im Arbeitsheft kontrollieren.

## Arbeitsweg

1. `Game.py` lesen; bereitgestellte Zustands-, Aktions- und Q-Tabellen-Hilfen testen.
2. TODO A: `choose_action` mit Exploration, Exploitation und legalen Zügen implementieren.
3. TODO B: `update_q_table` mit terminalem Target und legalem Bootstrap-Maximum ergänzen.
4. TODO C: `train_agent` aus den drei Codebausteinen übertragen; dann gegen X trainieren.
5. Lernkurve aus Ergebnisquoten erstellen und vorsichtig interpretieren.
6. Grenzen der Q-Tabelle, Deep RL, Sparse Rewards, Reward Hacking und Anwendungen diskutieren.
7. Erweiterungen wie wechselnde Startrolle und Self-Play planen.

**Wichtig:** Die Vorübung mit allen legalen Folgebrettern ist keine Suche, die der Agent in jedem Zug vollständig durchspielt. Während des Trainings wählt er eine Aktion; nur der tatsächliche Spielverlauf liefert die nächste Beobachtung und das Update.

Siehe das begleitende Arbeitsheft `Q_Learning_TicTacToe_Implementierung.docx` bzw. die PDF-Fassung.
