# Задание 4.
# Создайте функцию генератор чисел Фибоначчи


def fibonacci_generator():
    amount = 7
    a = 0
    b = 1
    for i in range(amount):
        yield b
        a, b = b, a + b


for number in (fibonacci_generator()):
    print(number, end=' ')
