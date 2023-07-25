# Задание 2.

#    Дан список повторяющихся элементов.
#    Вернуть список с дублирующимися элементами.
#    В результирующем списке не должно быть дубликатов.


some_list = [3, 'smile', 17, True, 5.42, 'smile', 78, 3, 'Ok', 'smile']
new_list = []
for item in some_list:
    if some_list.count(item) >= 2:
        new_list.append(item)
my_set = set(new_list)
print(list(my_set))
