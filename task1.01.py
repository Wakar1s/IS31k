# Задание 1 (пр7)
# импортируемые модули
import math

# вводные данные
print('Введите коэффициенты для уравнения')
print('ax^2 + bx + c = 0:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

# формула
D = b ** 2 - 4 * a * c
print('Дискриминант D = %.2f' % D)

if a == 0 and b == 0:
    print("Неразрешимое уравнение")
elif a == 0:
    print("Неквадратное уравнение")
elif D < 0:
  print("Случай комплексных корней")
elif b == 0 and c == 0:
    print("Нулевые корни: x1 = x2 = 0")
elif D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('x1 = %.2f \nx2 = %.2f' % (x1, x2))
elif D == 0:
    x = -b / (2 * a)
    print('x = %.2f' % x)
else:
    print('Корней нет')