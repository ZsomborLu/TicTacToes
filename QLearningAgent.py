"""Schüler-Gerüst: Die Kernlogik von Q-Learning selbst ergänzen.

Der Agent spielt immer O. Der zufällige Gegner X beginnt jede Trainingspartie.
get_state, get_valid_actions, get_next_states und get_q_values sind als
Hilfsmethoden bereits vorbereitet. choose_action und update_q_table sind die
Programmieraufträge; train_agent wird aus drei Codeblöcken des Arbeitshefts
übertragen.
"""

from copy import deepcopy
import random


class QLearningAgent:
    def __init__(self, game, alpha=0.2, gamma=0.9, epsilon=0.3,
                 epsilon_decay=0.9995, epsilon_min=0.02):
        """Startwerte für Umgebung, Hyperparameter und Q-Tabelle."""
        self.game = game
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

        self.reward_win = 1
        self.reward_loss = -1
        self.reward_draw = 0

        # Schlüssel: Tupelzustand. Wert: neun Aktionswerte für die Felder 0–8.
        self.q_table = {}
        self.rng = random.Random()

    def get_state(self, board):
        """Wandle eine veränderbare Liste von Listen in einen Tupelschlüssel um."""
        return tuple(tuple(row) for row in board)

    def get_valid_actions(self, board):
        """Liefere nur freie Felder als Aktionen 0 bis 8."""
        return [
            row * 3 + col
            for row in range(3)
            for col in range(3)
            if board[row][col] == " "
        ]

    def get_next_states(self, board, player="O"):
        """Erzeuge Kopien nach jedem legalen Zug; verändert das Original nicht.

        Für mögliche Agentenzüge wird player="O" verwendet. Mögliche X-Antworten
        untersucht man auf einem hypothetischen Brett nach einem O-Zug mit
        player="X". Im Training wird nur eine zufällige Antwort wirklich gespielt.
        """
        next_states = []
        for action in self.get_valid_actions(board):
            next_board = deepcopy(board)
            row, col = divmod(action, 3)
            next_board[row][col] = player
            next_states.append(next_board)
        return next_states

    def get_q_values(self, state):
        """Liefere neun Q-Werte; ein neuer Zustand startet mit lauter Nullen."""
        if state not in self.q_table:
            self.q_table[state] = [0.0] * 9
        return self.q_table[state]

    def choose_action(self, board=None):
        """TODO A: Eine legale Aktion mit epsilon-greedy auswählen."""
        if board is None:
            board = self.game.board

        valid_actions = self.get_valid_actions(board)
        if not valid_actions:
            raise ValueError("Für ein volles Brett gibt es keine legale Aktion.")

        state = self.get_state(board)
        q_values = self.get_q_values(state)

        # TODO A1: Mit Wahrscheinlichkeit epsilon zufällig aus valid_actions wählen.
        # TODO A2: Sonst den höchsten Q-Wert NUR unter valid_actions bestimmen.
        # TODO A3: Bei Gleichstand zufällig zwischen den besten legalen Zügen wählen.
        raise NotImplementedError("TODO A: choose_action vervollständigen")

    def update_q_table(self, state, action, reward, next_state=None, terminal=False):
        """TODO B: Genau Q(state, action) gemäss Q-Learning aktualisieren."""
        q_values = self.get_q_values(state)
        old_value = q_values[action]

        if terminal:
            # TODO B1: Für terminale Zustände ist target nur der unmittelbare Reward.
            target = None
        else:
            if next_state is None:
                raise ValueError("Für ein nicht-terminales Update ist next_state nötig.")
            next_actions = self.get_valid_actions(next_state)
            if not next_actions:
                raise ValueError("Ein terminaler Folgezustand braucht terminal=True.")

            next_q_values = self.get_q_values(next_state)
            # TODO B2: best_next_value = höchster Wert nur über next_actions.
            # TODO B3: target = reward + gamma * best_next_value.
            target = None

        # TODO B4: Q <- old_value + alpha * (target - old_value)
        #           und Ergebnis an q_values[action] speichern.
        raise NotImplementedError("TODO B: update_q_table vervollständigen")

    def train_agent(self, episodes=20_000, seed=None):
        """TODO C: Methode aus den drei Codebausteinen im Arbeitsheft übertragen."""
        raise NotImplementedError("TODO C: train_agent aus dem Arbeitsheft übertragen")
