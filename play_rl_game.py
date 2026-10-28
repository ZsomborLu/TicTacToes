"""Trainiere den implementierten Agenten und spiele danach gegen ihn."""
from Game import Game
from QLearningAgent import QLearningAgent


def main():
    game = Game()
    agent = QLearningAgent(game)
    episodes = 20_000

    print(f"Trainiere gegen zufälliges X ({episodes:,} Episoden)...".replace(",", "."))
    history = agent.train_agent(episodes=episodes, seed=7)
    window_size = 500
    print("\nFenster | Siegquote | Niederlagenquote | Remisquote")
    for start in range(0, len(history), window_size):
        window = history[start:start + window_size]
        n = len(window)
        wins = window.count("win") / n
        losses = window.count("loss") / n
        draws = window.count("draw") / n
        print(f"{start + 1:>5}–{start + n:<5} | {wins:>8.1%} | {losses:>15.1%} | {draws:>11.1%}")

    print("\nTraining abgeschlossen. Du spielst X; der Agent spielt O.")
    agent.epsilon = 0.0  # Während der Partie soll der Agent nicht mehr explorieren.
    game.set_agent(agent)
    game.play_game()


if __name__ == "__main__":
    main()
