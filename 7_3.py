string = input("Введите строку для проверки: ")
s_c = input("Введите проверочную строку: ")
count = 0
i = 1
while i != -1:
    i = string.find(s_c)
    if i >= 0:
        count += 1
    string = string[i+1:]

print(count)