import os
from random import randint

import getch
from colorama import Fore, Style


def generate_unique_numbers(count, minbound, maxbound):
    if count > maxbound - minbound + 1:
        raise ValueError('Incorrect input parameters')
    ret = []
    while len(ret) < count:
        new = randint(minbound, maxbound)
        if new not in ret:
            ret.append(new)
    return ret


def stop_and_print(txt=None, clr=True):
    if txt:
        print(txt)
    getch.getch()
    if clr:
        os.system('cls' if os.name == 'nt' else 'clear')


def comparing_cards(card1: object, card2: object) -> str:
    if card1 == card2:
        return 'Количество номеров равно'
    elif card1 > card2:
        return f'У игрока {card1} больше не зачеркнутых номеров'
    elif card1 < card2:
        return f'У игрока {card2} больше не зачеркнутых номеров'


def input_num():
    while True:
        try:
            col_comp = int(input('Введите количество игроков-компьютеров: '))
            if col_comp >= 0:
                break
            else:
                raise ValueError('Только положительные')
        except ValueError:
            print(f'{Fore.RED}Неверный ввод{Style.RESET_ALL}')

    while True:
        try:
            col_user = int(input('Введите количество игроков-людей: '))
            if col_user >= 0:
                break
            else:
                raise ValueError('Только положительные')
        except ValueError:
            print(f'{Fore.RED}Неверный ввод{Style.RESET_ALL}')

    return col_user, col_comp


def wins(winners: set | list):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\n\n\n{Fore.LIGHTGREEN_EX}{"Победитель:" if len(winners) == 1 else "Победители:"}')
    for gamer in winners:
        print(gamer)
    print('\n\n\n')
    stop_and_print()
