# Лабораторная работа №7
# Задание 1
a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

d = b ** 2 - 4 * a * c

try:
    if d < 0:
        print('Корней нет')
    elif d == 0:
        x = -b / (2 * a)
        print('x = ' + str(x))
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print('x1 = ' + str(x1))
        print('x2 = ' + str(x2))

except ZeroDivisionError:
    print('Неразрешимое уравнение')
