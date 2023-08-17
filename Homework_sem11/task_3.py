# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц


class Matrix:
    def __init__(self, rows, columns, data):
        self.rows = rows
        self.columns = columns
        self.data = data

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must be the same size")
        res = Matrix(self.rows, self.columns, self.data)
        for i in range(self.rows):
            for j in range(self.columns):
                res.data[i][j] = self.data[i][j] + other.data[i][j]
        return res

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("The number of columns of the 1-st matrix must be equal to the number of rows of the other")
        res = Matrix(self.rows, self.columns, self.data)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    res.data[i][j] += self.data[i][k] * other.data[k][j]
        return res

    def __eq__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must be the same size")
        else:
            for i in range(self.rows):
                for j in range(other.columns):
                    if self.data[i][j] != other.data[i][j]:
                        return False
            return True

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


if __name__ == '__main__':
    m1 = Matrix(2, 2, [[1, 2], [3, 4]])
    m2 = Matrix(2, 2, [[2, 1], [0, 1]])

    result = m1.__eq__(m2)
    print(result)

    print(m1)
    print()
    print(m2)
    print()

    print(m1 + m2)
    print()

    print(m1 * m2)


