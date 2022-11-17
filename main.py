#второе и третье задание
import math

try:
    a, b, c = map(int, input("Введите A, B, C: ").split())
except ValueError:
    print("Вы возможно ввели буквы или какую-нибудь другую ерунду, пишите цифры!")

#a = int(input('Введите А: '))
#b = int(input('Введите B: '))
#c = int(input('Введите C: '))

D = b * b - (4 * a * c)
if D < 0:
    print("Случай комплексных корней.")
    raise SystemExit
elif D == 0:
    try:
        x1 = -c / b
        print(f"Есть один корень: {x1}")
        raise SystemExit
    except ZeroDivisionError:
        print("Неразрешимое уравнение")
        raise SystemExit
else:
    try:
        x1 = (-b + math.sqrt(D)) / (2 * a)
    except ZeroDivisionError:
        print("Неквадратное уравнение")
        raise SystemExit

    try:
        x2 = (-b - math.sqrt(D)) / (2 * a)
    except ZeroDivisionError:
        print("1")
        raise SystemExit

x1 = (-b + math.sqrt(D)) / (2 * a)
x2 = (-b - math.sqrt(D)) / (2 * a)
"""if x1 <= 0 and x2 <= 0:
    print("0")
elif x2 <= 0:
    print("0")
"""
print(f"Есть два корня: \nx1 = {int(x1)} \nx2 = {int(x2)}")
