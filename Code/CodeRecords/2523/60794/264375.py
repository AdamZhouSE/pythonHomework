a = eval(input())
for i in range(len(a)):
    single = []
    x = i
    y = 0
    while True:
        if y > len(a[0]) - 1 or x > len(a) - 1:
            break
        else:
            single.append(a[x][y])
            x = x + 1
            y = y + 1
    list.sort(single)
    x = i
    y = 0
    t = 0
    while True:
        if y > len(a[0]) - 1 or x > len(a) - 1:
            break
        else:
            a[x][y] = single[t]
            x = x + 1
            y = y + 1
            t = t + 1
for i in range(1, len(a[0])):
    single = []
    y = i
    x = 0
    while True:
        if y > len(a[0]) - 1 or x > len(a) - 1:
            break
        else:
            single.append(a[x][y])
            x = x + 1
            y = y + 1
    list.sort(single)
    y = i
    x = 0
    t = 0
    while True:
        if y > len(a[0]) - 1 or x > len(a) - 1:
            break
        else:
            a[x][y] = single[t]
            x = x + 1
            y = y + 1
            t = t + 1
print(a)