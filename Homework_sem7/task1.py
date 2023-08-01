# Задание 1.

# Создайте функцию для сортировки файлов по директориям: видео, изображение, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

__all__ = ['sort_files']


from os import listdir, mkdir, chdir
from pathlib import Path

START_DIR = '/Homework_sem7'


def get_extension(ext: list[str]) -> list[str]:
    ext = set(map(lambda x: x.split('.')[-1], ext))
    return list(ext)


def sort_files(work_dir: str) -> None:
    ext = get_extension(listdir(Path(work_dir)))
    chdir(Path(work_dir))
    for ext in ext:
        try:
            mkdir(ext)
        except FileExistsError:
            pass
    for file in filter(lambda x: x.find('.') != -1, listdir()):
        prev = Path(file)
        prev.replace(Path.cwd() / file.split('.')[-1] / prev)


sort_files(START_DIR)
