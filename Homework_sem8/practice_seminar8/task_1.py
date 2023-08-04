# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате json.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.


import json


def create_json(file_path: str, json_path: str) -> None:
    file_dict = {}
    with open(file_path, 'r', encoding='utf-8') as my_file:
        for line in my_file:
            name, num = line.split('|')
            file_dict[name.capitalize()] = float(num)

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(file_dict, json_file, ensure_ascii=False, indent=2)


create_json('for_task1.txt', 'for_task1.json')
