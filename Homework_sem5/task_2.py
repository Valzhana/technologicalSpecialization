# Задание 2.

# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def get_path():
    path = "C:/Thecode/Media/статья.txt"
    return path


def get_tuple_from_path(path: str) -> tuple:
    extension = path.split('.')[-1]
    name = path.split('/')[-1].split('.')[-2]
    file_path = '/'.join(path.split('.')[0].split('/')[:-1])
    path_tuple = file_path, name, extension
    print(path_tuple)
    return path_tuple


get_tuple_from_path(get_path())
