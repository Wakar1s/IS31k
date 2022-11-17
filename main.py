from math import sqrt
from typing import NoReturn


def work7__1() -> NoReturn:
    a, b, c = map(int, input("Введите три числа через пробел: ").split())
    D: int = b ** 2 - 4 * a * c

    if not a and not b:
        print("Неразрешимое уравнение")
    elif not a:
        print("Неквадратное уравнение")
    elif D < 0:
        print("Случай комплексных корней")
    elif not b and not c:
        print("Нулевые корни: x1 = 0\n x2 = 0")
    elif D > 0:
        print(f"x1: {(-b + sqrt(D)) / (2 * a)}\nx2: {(-b - sqrt(D)) / (2 * a)}")
    elif not D:
        print(f"x: {-b / 2 * a}")


def work7__2() -> NoReturn:
    work7__1()


def work7__3() -> NoReturn:
    s1, s2 = map(str, input("Введите две строки через пробел: ").split())

    count: int = 0
    ind: int = 1
    while ind != -1:
        ind = s1.find(s2)
        if ind >= 0:
            count += 1
        s1 = s1[ind + 1:]
    print(f"Вывод: {str(count)}")


def work8__1() -> NoReturn:
    square = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15,
              'F': 21, 'G': 22, 'H': 23, 'I': 24, 'K': 25,
              'L': 31, 'M': 32, 'N': 33, 'O': 34, 'P': 35,
              'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
              'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55,
              }
    vr: str = input("Что вы хотите сделать?\n1) Зашифровать\n2) Расшифровать\nВаш выбор: ")

    match vr:
        case "1":
            strng: str = input("Введите строчку: ").upper()

            mess: str = ''
            list_mess: list = list(strng)
            for i in strng:
                if i in square:
                    mess += str(square.get(i, 0))
                elif i not in square:
                    print('Введите корректные данные')
                    break
                else:
                    mess += (i + i)

            with open(".last string", "w") as file:
                file.write(mess)
                file.close()
            print("Шифр записан в файл \".last string\"")
        case "2":
            with open(".last string", "r") as file:
                intgr: str = file.read()
                file.close()

            if not intgr.isnumeric():
                print("Введите числа!")
                quit()
            else:
                ss: str = ''
                list_ss: list = []
                step: int = 2
                for i in range(0, len(intgr), 2):
                    list_ss.append(intgr[i:step])
                    step += 2
                list_ss: list = list(map(int, list_ss))
                key_square: list = list(square.keys())
                val_square: list = list(square.values())

                for i in list_ss:
                    if i in val_square:
                        i = val_square.index(i)
                        ss += key_square[i]
                    elif i not in val_square:
                        print("Введите числа!")
                    else:
                        ss += i[0:1]
                print(ss)
        case _:
            print("Ошибка!")


def work8__2() -> NoReturn:
    work8__1()


def work8__3() -> NoReturn:
    print("Будет в отчете")


if __name__ == '__main__':
    variant = input("Введите вариант(7-8): ")
    match variant:
        case "7":
            work = input("Введите задание(1-3): ")

            match work:
                case "1":
                    work7__1()
                case "2":
                    work7__2()
                case "3":
                    work7__3()
                case _:
                    print("Нет такого варианта")
        case "8":
            work8__1()
