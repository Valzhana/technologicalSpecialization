# Задание №8
# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

input_rows = int(input('Enter the number of rows: '))
MIN_ROWS = 1
MAX_ROWS = input_rows

while MIN_ROWS <= MAX_ROWS:
    print((MAX_ROWS - MIN_ROWS) * ' ' + MIN_ROWS * '*' + (MIN_ROWS - 1) * '*')
    MIN_ROWS += 1
