size = int(input())
if size == 1:
    print(1)
else:
    l = []
    i = 0
    while i < size:
        temp = []
        j = 0
        while j < size:
            temp.append(1)
            j += 1
        i += 1
        l.append(temp)
    i = 1
    while i < size:
        j = 1
        while j < size:
            l[i][j] = l[i - 1][j] + l[i][j - 1]
            j += 1
        i += 1
    print(l[size - 1][size - 1])
