# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

# Задание 2, семинар 6.
# Известно, что на доске 8х8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8-ми ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга - верните истину, а если бьют - ложь.


import random as rnd


class MyException(Exception):
    pass


class QuantityException(MyException):
    def __init__(self, cells: int, queens: int):
        self.cells = cells
        self.queens = queens

    def __str__(self):
        return f'The number of queens and their positions must be equal to {self.cells}'


class CoordinateException(MyException):
    def __init__(self, min_coord, max_coord):
        self.min_coord = min_coord
        self.max_coord = max_coord

    def __str__(self):
        return f'The coordinate must be a number from {self.min_coord} to {self.max_coord}'


class Chess:

    def __init__(self, positions: list[tuple]):
        self.positions = positions
        self.queens = 8
        self.cells = 8
        self.min_coord = 1
        self.max_coord = 8

    def check_queen_beats(self) -> bool:
        result = True
        if len(self.positions) != self.queens:
            raise QuantityException(self.cells, self.queens)
        for pos in self.positions:
            for item in pos:
                if item < self.min_coord or item > self.max_coord:
                    raise CoordinateException(self.min_coord, self.max_coord)
        else:
            for i in range(self.queens - 1):
                if not result:
                    break
                row_1, col_1 = self.positions[i]
                for j in range(i + 1, self.queens):
                    row_2, col_2 = self.positions[j]
                    if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                        result = False
                        break
        return result

    def success_positions(self) -> list[tuple[int, int]]:
        result = []
        for i in range(self.cells):
            result.append((i, rnd.randint(1, self.cells)))
        return result


if __name__ == '__main__':
    my_chess = Chess([(8, 4), (7, 3), (8, 2), (2, 1), (3, 1), (8, 4), (5, 1), (5, 3)])
    print(my_chess.check_queen_beats())
