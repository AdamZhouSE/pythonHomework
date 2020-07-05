num = int(input())
res = 0
for i in range(1, num + 1):
    if i == 1:
        res = res + 10
    elif i == 2:
        res = res + 9 * 9
    else:
        add = 81
        for j in range(1, i - 1):
            add = add * (9 - j)
        res = res + add
print(res)