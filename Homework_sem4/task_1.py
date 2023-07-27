# Задание 1

# Напишите функцию для транспонирования матрицы


def get_matrix():
    new_matrix = [[1, 2, 3], [4, 9, 5], [2, 9, 7], [2, 1, 1]]
    return new_matrix


def get_transpose_matrix(matrix):
    rows = zip(*matrix)
    t_matrix = []
    for row in rows:
        transpose_matrix = list(row)
        t_matrix.append(transpose_matrix)
    return t_matrix


def main():
    result = get_transpose_matrix(get_matrix())
    for item in result:
        print(item)


main()
