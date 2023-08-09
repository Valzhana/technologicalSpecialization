# Задание 2.
import os.path

# Напишите следующие функции:
# Нахождение корней квадратного уравнения.
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


__all__ = ['get_roots_of_equation', 'generate_csv_file', 'get_nums_from_csv', 'save_to_json']

from os.path import exists
from typing import Callable
import random
import csv
import json


def get_nums_from_csv(func: Callable) -> Callable:
    def wrapper():
        file_name = f'{generate_csv_file.__name__}.csv'
        results = []
        with open(file_name, 'r') as new_file:
            reader = csv.reader(new_file)
            for row in reader:
                a, b, c = map(int, row)
                results.append(func(a, b, c))
        return results

    return wrapper


def save_to_json(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        file_path = f'{func.__name__}.json'
        data = []
        if exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
        result = func(*args, **kwargs)
        cur_data = {
            'args': args,
            **kwargs,
            'result': result
        }
        data.append(cur_data)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)
        return result

    return wrapper


@get_nums_from_csv
@save_to_json
def get_roots_of_equation(a: float, b: float, c: float) -> None | float | tuple[float, float]:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return x1, x2


def generate_csv_file():
    path_name = f'{generate_csv_file.__name__}.csv'
    with open(path_name, 'w', newline='') as file_csv:
        writer = csv.writer(file_csv, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(random.randint(100, 1000)):
            writer.writerow([random.randint(1, 100) for _ in range(3)])


if __name__ == '__main__':
    generate_csv_file()
    get_roots_of_equation()
