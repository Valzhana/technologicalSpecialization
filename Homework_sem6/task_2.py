# Задание 2.
# Добавьте в пакет, созданный на семинаре, шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях.
# Известно, что на доске 8х8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8-ми ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга - верните истину, а если бьют - ложь.


# Задача 3.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки
# ферзей в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки.


import random as rnd

__all__ = ['check_queen_beats', 'success_positions']

QUEENS: int = 8
CELLS: int = 8


def check_queen_beats(positions: list[tuple]) -> bool:
    result = True
    if len(positions) != QUEENS:
        result = False
    else:
        for i in range(QUEENS - 1):
            if not result:
                break
            row_1, col_1 = positions[i]
            for j in range(i + 1, QUEENS):
                row_2, col_2 = positions[j]
                if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                    result = False
                    break
    return result


def success_positions() -> list[tuple[int, int]]:
    result = []
    for i in range(CELLS):
        result.append((i, rnd.randint(0, CELLS - 1)))
    return result


if __name__ == '__main__':
    print(check_queen_beats([(8, 6), (7, 3), (7, 2), (7, 1), (3, 2), (1, 4), (5, 1), (3, 1)]))
    print(f'Successful positions: {success_positions()}')
