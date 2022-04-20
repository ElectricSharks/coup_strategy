from coup.player import Player
from coup.game import Game
from coup.strategy import HonestStrategy, ManualInputStrategy


def main():
    honest_strategy = HonestStrategy()
    manual_input = ManualInputStrategy()
    players = [
        Player("Me!", manual_input),
        Player("Honest Player 2", honest_strategy),
        Player("Honest Player 3", honest_strategy),
    ]
    new_game = Game(players)
    new_game.play()


if __name__ == "__main__":
    main()
