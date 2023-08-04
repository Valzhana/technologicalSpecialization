# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор
# и уровень доступа (от 1 до 7)
# После каждого ввода добавляйте новую информацию в json файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключом для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уе записанные в файл данные должны сохраняться.
import json
import os

js_file = 'for_task2.json'


def add_data_to_json(json_file):
    user_ids = set()
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8'):
            data = json.load(json_file)
            for user in data.values():
                user_ids.update(user.keys())
    else:
        data = {str(access_level): dict() for access_level in range(1, 8)}

    while True:
        name = input('Enter your name: ')
        if not name:
            break
        id_input = input('Enter your id: ')
        access_level = input('Enter access level: ')
        if id_input in user_ids:
            continue
        data[access_level][id_input] = name
        with open(json_file, 'w', encoding='utf-8') as data_file:
            json.dump(data, data_file, indent=2)


add_data_to_json(js_file)
