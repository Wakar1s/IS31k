import math
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
D = b ** 2 - 4 * a * c
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
    print(x1)
    print(x2)
elif D == 0:
  x = -b / 2 * a
  print (x)