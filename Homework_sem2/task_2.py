# Задание 2.

# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def get_input():
    input_number = int(input("Enter decimal number: "))
    return input_number


def converter():
    decimal_number = get_input()
    HEXADECIMAL_DIGITS = "0123456789ABCDEF"
    hexadecimal_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_digit = HEXADECIMAL_DIGITS[remainder]
        hexadecimal_number = hexadecimal_digit + hexadecimal_number
        decimal_number //= 16
    return hexadecimal_number


print(converter())
print(hex(get_input()))



