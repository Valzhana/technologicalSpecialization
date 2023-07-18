# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

MAX_FACTOR = 10
factor = 2
number = 2

while number < MAX_FACTOR:
    if factor <= MAX_FACTOR:
        print(f"{number}x{factor} = {number * factor}")
        factor += 1
    else:
        print(" ")
        factor = 2
        number += 1
        continue
