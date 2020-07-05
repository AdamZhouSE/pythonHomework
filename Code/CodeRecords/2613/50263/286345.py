import math


n = int(input())
for i in range(n):
    connell = []
    res = 0
    count = int(input())
    for k in range(count):
        x = True
        for j in range(count):
            if k == j*(j+1)/2:
                x = False
        if x:
            res += 2
        else:
            res += 1
        connell.append(res)
    for j in range(count):
        if j != count - 1:
            print(connell[j], end=' ')
        else:
            print(connell[j])
        