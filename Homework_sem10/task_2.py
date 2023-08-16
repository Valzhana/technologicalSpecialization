# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.


# Создайте функцию для сортировки файлов по директориям: видео, изображение, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


from pathlib import Path
from os import listdir, chdir, mkdir


class Directory:
    def __init__(self, path):
        self.path = path

    def get_extension(self, ext):
        ext = set(map(lambda x: x.split('.')[-1], ext))
        return list(ext)

    def sort_files(self) -> None:
        ext = self.get_extension(listdir(Path(self.path)))
        chdir(Path(self.path))
        for ext in ext:
            try:
                mkdir(ext)
            except FileExistsError:
                pass
        for file in filter(lambda x: x.find('.') != -1, listdir()):
            prev = Path(file)
            prev.replace(Path.cwd() / file.split('.')[-1] / prev)


if __name__ == '__main__':
    my_directory = Directory('.')
    my_directory.sort_files()
