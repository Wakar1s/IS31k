square = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15,
          'F': 21, 'G': 22, 'H': 23, 'I': 24, 'K': 25,
          'L': 31, 'M': 32, 'N': 33, 'O': 34, 'P': 35,
          'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
          'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55,
}

n = input('Text\n').upper()
m = input('int\n').upper()

def getNum(n):
    mess = ''
    l_mess = list(n)
    for i in n:
        if i in square:
            mess += str(square.get(i, 0))
        elif i not in square:
            print('Введите корректные данные')
        else:
            mess += (i + i)
    return mess


def getStr(n):
    if n.isnumeric() != True:
        return f'Введите корректные данные'
    else:
        ss = ''
        list_ss = []
        step = 2
        for i in range(0, len(n), 2):
            list_ss.append(n[i:step])
            step += 2
        list_ss = list(map(int, list_ss))
        key_square = list(square.keys())
        val_square = list(square.values())

        for i in list_ss:
            if i in val_square:
                i = val_square.index(i)
                ss += key_square[i]
            elif i not in val_square:
                return f'Введите корректные данные'
            else:
                ss += i[0:1]
        return ss


print(getNum(n))
print(getStr(m))