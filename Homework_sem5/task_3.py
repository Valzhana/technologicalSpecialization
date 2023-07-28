# Задание 3.
# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой
# длины: имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


def dict_name_bonus(name_lst, rate_lst, bonus_lst):
    result_dict = {name: rate * (1 + float(bonus.strip('%')) / 100) for name, rate, bonus
                   in zip(name_lst, rate_lst, bonus_lst)}
    return result_dict


names = ['Martha', 'Mark', 'Pol']
rates = [500, 2000, 1000]
bonuses = ['20.8%', '32.5%', '10%']

print(dict_name_bonus(names, rates, bonuses))
