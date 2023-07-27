# Задание 2.

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def get_dictionary(**arguments):
    new_dict = {}
    for key, value in arguments.items():
        if arguments[key].__hash__:
            new_dict[key] = value
        else:
            new_dict[str(key)] = value
    return new_dict


def main():
    print(get_dictionary(name='Mark', nickname='Lucky', weight=55.5,
                         months=['January', 'February', 'March'],
                         courses={'python': 'ver 3.11', 'c#': 'ver 2.5'}))


main()
