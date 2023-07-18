# Задание 2.
#
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
#     Дано a, b, c - стороны предполагаемого треугольника.
#     Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
#     Если хотя бы в одном случае отрезок окажется больше суммы двух других,
#     то треугольника с такими сторонами не существует.
#     Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

side_a = int(input('Enter first side: '))
side_b = int(input('Enter second side: '))
side_c = int(input('Enter third side: '))

if side_c < side_a + side_b and side_b < side_a + side_c and side_a < side_c + side_b:
    print('This is triangle')
    if side_c == side_b and side_b == side_a and side_a == side_c:
        print('This triangle is equilateral')
    elif side_c == side_b or side_b == side_a or side_c == side_a:
        print('This triangle is isosceles')
    else:
        print('This triangle is versatile')
else:
    print('There is no triangle with such sides')
