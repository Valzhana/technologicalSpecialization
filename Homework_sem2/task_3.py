from fractions import Fraction


# Задание 3.

# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions


def sum_prod_fractions(first_fraction, second_fraction):
    first_numer, first_denominator = map(int, first_fraction.split("/"))
    second_numer, second_denominator = map(int, second_fraction.split("/"))

    sum_frac_numer = first_numer * second_denominator + second_numer * first_denominator
    sum_frac_deno = first_denominator * second_denominator
    sum_fractions = (sum_frac_numer, sum_frac_deno)

    prod_frac_numer = first_numer * second_numer
    prod_frac_denominator = first_denominator * second_denominator
    prod_fractions = (prod_frac_numer, prod_frac_denominator)

    return sum_fractions, prod_fractions


first_frac: str = input("Enter the first fraction with a slash: ")
second_frac: str = input("Enter the second fraction with a slash: ")
sum_frac, prod_frac = sum_prod_fractions(first_frac, second_frac)

print(f"Sum of fractions {first_frac} и {second_frac} - {sum_frac[0]}/{sum_frac[1]}")
print(f"Product of fractions {first_frac} и {second_frac} - {prod_frac[0]}/{prod_frac[1]}")


fract_1 = Fraction(int(first_frac[0]), int(first_frac[2]))
fract_2 = Fraction(int(second_frac[0]), int(second_frac[2]))
sum_fractions = fract_2 + fract_1
prod_fractions = fract_2 * fract_1
print(Fraction(sum_fractions))
print(Fraction(prod_fractions))
