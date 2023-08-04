# Задание 2.

#   Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.

#       Результаты обхода сохраните в файлы json, csv и pickle.
#       Для дочерних объектов указывайте родительскую директорию.
#       Для каждого объекта укажите файл это или директория.
#       Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
#       с учётом всех вложенных файлов и директорий.


import os
import json
import csv
import pickle

__all__ = ['walk_over_directory']


def get_size(path):
    total = 0
    for dir_path, dir_names, filenames in os.walk(path):
        for file in filenames:
            file_path = os.path.join(dir_path, file)
            total += os.path.getsize(file_path)
    return total


def walk_over_directory(direct_path):
    results = []
    for root, dirs, files in os.walk(direct_path):
        for name in files:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root,
                            "is_file": True,
                            "name": name,
                            "size_in_bytes": os.path.getsize(full_path)})

        for name in dirs:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root,
                            "is_file": False,
                            "name": name,
                            "size_in_bytes": get_size(full_path)})

    with open("output.json", "w") as json_file:
        json.dump(results, json_file)

    with open("output.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    with open("output.pickle", "wb") as pickle_file:
        pickle.dump(results, pickle_file)


walk_over_directory(".")
