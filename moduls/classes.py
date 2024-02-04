from random import shuffle
from colorama import Fore, Style
from moduls.functions import generate_unique_numbers

from random import randint


class Card:
    __rows = 3
    __cols = 9
    __nums_in_row = 5
    __data = None
    __emptynum = 0
    __crossednum = -1
    lose = False

    def __init__(self, name: str):
        self.name = name
        uniques_count = self.__nums_in_row * self.__rows
        uniques = generate_unique_numbers(uniques_count, 1, 90)

        self.__data = []
        for i in range(0, self.__rows):
            tmp = sorted(uniques[self.__nums_in_row * i: self.__nums_in_row * (i + 1)])
            empty_nums_count = self.__cols - self.__nums_in_row
            for j in range(0, empty_nums_count):
                index = randint(0, len(tmp))
                tmp.insert(index, self.__emptynum)
            self.__data += tmp

    def __str__(self):
        delimiter = '--------------------------'
        ret = delimiter + '\n'
        for index, num in enumerate(self.__data):
            if num == self.__emptynum:
                ret += '  '
            elif num == self.__crossednum:
                ret += ' -'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % self.__cols == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + delimiter

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
        for index, item in enumerate(self.__data):
            if item == num:
                self.__data[index] = self.__crossednum

    def closed(self) -> bool:
        return set(self.__data) == {self.__emptynum, self.__crossednum}


class Game:
    __usercards = []
    __compcards = []
    __kegs = []
    winners = []
    lose = []

    def __init__(self, users=1, comps=1):
        if users + comps < 2:
            raise ValueError(f'{Fore.RED}[ERROR] Участников игры должно быть не менее 2')
        for i in range(users):
            name_user = input(f"Введите имя игрока {i + 1}:{Fore.GREEN} ")
            print(Style.RESET_ALL, end='')
            self.__usercards.append(Card(name=name_user))
        for i in range(comps):
            self.__compcards.append(Card(name=f"Компьютер {i + 1}"))

        self.__kegs = list(range(1, 91))
        shuffle(self.__kegs)

    def play_round(self):
        keg = self.__kegs.pop()
        print(f'{Fore.LIGHTGREEN_EX}Новый бочонок: {keg} (осталось {len(self.__kegs)}){Style.RESET_ALL}\n')
        for card in self.__compcards:
            print(f'Карточка игрока {card.name}\n{card}')
            card.cross_num(keg)
            if card.closed():
                self.winners.append(card.name)
        for card in self.__usercards:
            if not card.lose:
                print(f'{Fore.GREEN}Карточка игрока {card.name}{Style.RESET_ALL}\n{card}')
                user_answer = input('Зачеркнуть цифру? (y/n)').lower().strip()
                if ((user_answer == 'y' and not keg in card) or
                        (user_answer != 'y' and keg in card)):
                    card.lose = True
                    self.lose.append(card)
                    print(f'{Fore.BLUE}Игрок {card.name} выбыл{Style.RESET_ALL}')
            else:
                print(f'{Fore.BLUE}Игрок {card.name} выбыл{Style.RESET_ALL}')

    def check_gamer(self):
        return len(self.lose) == len(self.__usercards)