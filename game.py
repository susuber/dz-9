import os

import getch
from colorama import Fore, Style

from moduls.classes import Game
from moduls.functions import stop_and_print, input_num, wins


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    col_user, col_comp = input_num()
    game = Game(users=col_user, comps=col_comp)
    game_comp = True
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        game.play_round()
        if game.winners:
            wins(game.winners)
            break

        if not game_comp:
            stop_and_print("Нажмите любую клавишу...")

        players = game.chek_players()

        match len(players):
            case 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'\n\n\n{Fore.LIGHTGREEN_EX}Победителей нет{Style.RESET_ALL}\n\n\n')
                stop_and_print()
                break
            case 1:
                wins([players.pop().name])
                break

        if game.check_gamer() and game_comp:
            ans = input(f"{Fore.LIGHTRED_EX}Все игроки проиграли продолжить игру компьютеров (y/N): ")
            if ans.lower() not in ['y', 'yes']:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'\n\n\n{Fore.LIGHTGREEN_EX}Спасибо за игру{Style.RESET_ALL}\n\n\n')
                stop_and_print()
                break
            else:
                game_comp = False


if __name__ == '__main__':
    main()










