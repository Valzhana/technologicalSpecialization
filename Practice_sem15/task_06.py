# Задание №6
# 📌 Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя
# логирование.

from collections import namedtuple
from pathlib import Path
import logging
import argparse

logging.basicConfig(filename='task_06.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

File = namedtuple('File', 'name, extension, is_dir, parent_dir')


def parse():
    parser = argparse.ArgumentParser(prog='read_dir',
                                     description='Получение информации о файлах и директориях',
                                     epilog='read_dir("C:/Users/User/PycharmProjects/pythonProject'
                                            '/technologicalSpecialization/Practice_sem15")')
    parser.add_argument('-p', '--path', type=Path, default='.', help='Путь до директории на ПК')
    args = parser.parse_args()
    return read_dir(f'{args.path}')


def read_dir(path: Path):
    for file in path.iterdir():
        new_file = File(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(new_file)
        if new_file.is_dir:
            read_dir(Path(new_file.parent_dir) / new_file.name)


if __name__ == '__main__':
    print(read_dir(Path('C:/Users/User/PycharmProjects/pythonProject/technologicalSpecialization/Practice_sem15')))
