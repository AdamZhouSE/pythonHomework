a = list(map(int, list(input())))
a.sort()
flag = False
for i in range(0, 20):
    b = list(map(int, list(str(2**i))))
    b.sort()
    if a == b:
        flag = True
print(flag)