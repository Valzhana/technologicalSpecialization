# Дорабатываем класс прямоугольник из прошлого семинара
# Добавьте возможность сложения и вычитания. При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.


class Rectangle:
    """
    Takes two parameters - two sides of rectangle and returns its perimeter and area.
    If only one side is passed to the class instance, then we consider this rectangle to be a square.
    """
    def __init__(self, side_a: float, side_b: float = None):
        self.side_a = side_a
        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def get_perimeter(self) -> float:
        return 2 * self.side_a + 2 * self.side_b

    def get_area(self) -> float:
        return self.side_a * self.side_b


class RectanglePro(Rectangle):
    """
    The class inherits from 'Rectangle' and works with two rectangles
    """
    sum_perimeter = None

    def __add__(self, other):
        """
        This method adds perimeters and sides of the rectangles
        """
        self.sum_perimeter = self.get_perimeter() + other.get_perimeter()
        side_a = self.side_a + other.side_a
        side_b = self.sum_perimeter / 2 - side_a
        return RectanglePro(float(side_a), float(side_b))

    def __sub__(self, other):
        """
        This method subtracts perimeters and sides of the rectangles
        """
        if self.get_perimeter() < other.get_perimeter():
            self, other = other, self
            diff = self.get_perimeter() - other.get_perimeter()
            side_a = abs(self.side_a - other.side_a)
            side_b = diff / 2 - side_a
            return RectanglePro(float(side_a), float(side_b))

    def __str__(self):
        return f' The perimeter of the rectangle is {self.get_perimeter()}'


if __name__ == '__main__':
    rectangle_1 = RectanglePro(2, 3)
    rectangle_2 = RectanglePro(5)
    print(rectangle_1)
    print(rectangle_2)

    rectangle_sum = (rectangle_1 + rectangle_2)
    print(rectangle_sum.get_perimeter())
    print(rectangle_sum.side_a, rectangle_sum.side_b)

    rectangle_diff = rectangle_1 - rectangle_2
    print(rectangle_diff.get_perimeter())
    print(rectangle_diff.side_a, rectangle_diff.side_b)

    print(Rectangle.__doc__)
    print(RectanglePro.__doc__)
    print(rectangle_1.__add__.__doc__)
