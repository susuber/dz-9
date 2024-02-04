import os

from moduls.classes import Game


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round()
        os.system('cls' if os.name == 'nt' else 'clear')
        if score == 1:
            print('You win')
            break
        elif score == 2:
            print('You lose')
            break








