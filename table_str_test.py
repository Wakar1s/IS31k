a = (input())
b = (input())
n = 0

for i in range(len(a) - len(b) + 1):
    if a[i:i + len(b)] == b:
        n += 1
print(n)