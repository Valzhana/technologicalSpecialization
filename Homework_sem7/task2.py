#   Задание 2.
#
# Напишите функцию группового переименования файлов. Она должна:

# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
#     Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
#     Например для диапазона [3, 6] берутся буквы с 3 по 6 из - исходного имени файла. К ним прибавляется желаемое
#     конечное имя, если оно передано. Далее счётчик файлов и расширение.

#   - 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

__all__ = ['rename_files']


import os


END_NAME = '_new'
dir_path = '/Homework_sem7/names'
EXTENSION_START = '.txt'
EXTENSION_END = '.py'
NAME_RANGE = (3, 7)


def rename_files(dir_files: str, final_name: str, file_ext_start: str,
                 file_ext_end: str, range_start: tuple) -> None:
    os.chdir(path=dir_files)
    file_list = os.listdir(path=dir_files)
    count = 1
    for i in file_list:
        start_name = str(os.path.splitext(i)[0])[range_start[0]:range_start[1]]
        fileExtension = os.path.splitext(i)[1]
        if fileExtension == file_ext_start:
            fileExtension = file_ext_end
            os.rename(i, start_name + final_name + str(count) + fileExtension)
            count += 1
        else:
            continue


rename_files(dir_path, END_NAME, EXTENSION_START, EXTENSION_END, NAME_RANGE)
