def equation(a, b, c):
    disc = b ** 2 - 4 * a * c
    print('Дискриминант = ' + str(disc))

    if disc > 0:
        x1 = (-b + disc ** 0.5) / (2 * a)
        x2 = (-b - disc ** 0.5) / (2 * a)
        print('x1 = ' + str(x1))
        print('x2 = ' + str(x2))
    elif disc == 0:
        x = -b / (2 * a)
        print('x = ' + str(x))
    elif disc < 0:
        print('Корней нет')

print('Написать программу решения квадратного уравнения ax^2 + bx + c = 0')

a = float(input())
b = float(input())
c = float(input())

if a == 0 and b == 0 and c == 0:
    print('Решения нет, так как уравнение линейное')
else:
    equation(a, b, c)
