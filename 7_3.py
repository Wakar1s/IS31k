s1 = input("Строка 1: ")
s2 = input("Строка 2: ")
count = 0
ind = 1
while ind != -1:
    ind = s1.find(s2)
    if ind >= 0:
        count += 1
    s1 = s1[ind+1:]
print("Вывод:" + str(count))