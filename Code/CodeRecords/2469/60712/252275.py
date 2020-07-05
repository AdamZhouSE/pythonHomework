n = int(input())
l = []
for i in range(n):
    temp = list(input())
    temp.sort()
    l.append(temp)
for i in range(n):
    dif = 1
    for j in range(len(l[i]) - 1):
        if l[i][j] != l[i][j + 1]:
            dif += 1
    # length of string
    for j in range(dif, len(l[i])):
        find = False
        for k in range(len(l[i])):

            if j + k <= len(l[i]):
                d = 1
                for m in range(k, j + k - 1):
                    if l[i][m] != l[i][m + 1]:
                        d += 1
                if d==dif:
                    find=True
                    print(j)
                    break
            if find:
                    break
        if find:
            break

