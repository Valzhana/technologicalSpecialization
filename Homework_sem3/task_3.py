# Задание 3.


# В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

def get_text():
    some_string = "There are three distinct numeric types: integers, floating point numbers, and complex numbers. " \
                  "In addition, Booleans are a subtype of integers. Integers have unlimited precision. " \
                  "Floating point numbers are usually implemented using double in C; information about the precision " \
                  "and internal representation of floating point numbers for the machine on which your program " \
                  "is running is available in sys.float_info. Complex numbers have a real and imaginary part, " \
                  "which are each a floating point number. To extract these parts from a complex number z, use z.real " \
                  "and z.image. (The standard library includes the additional numeric types fractions.Fraction, " \
                  "for rationals, and decimal.Decimal, for floating-point numbers with user-definable precision.)"
    return some_string


def ten_popular_words(text: str):
    delete = "0123456789.,!?;:-[]/{}()='_"
    for i in delete:
        text = text.replace(i, "")
    text = text.lower().split()
    words = []
    for i in range(len(text)):
        count = 0
        for word in text:
            if text[i] == word:
                count += 1
        words.append(str(count) + " - " + text[i])
        words = list(set(words))
        words = sorted(words)[::-1][:10:]

    return words


print(ten_popular_words(get_text()))
