from python.game.player import Player
from python.game.game import Game
from python.game.strategy import HonestStrategy


def main():
    honest_strategy = HonestStrategy()
    players = [Player("Honest Player 1", honest_strategy), Player("Honest Player 2", honest_strategy), Player("Honest Player 3", honest_strategy)]
    game = Game(players)
    for _ in range(5):
        game.play()
        game.reset()
    


if __name__ == "__main__":
    main()