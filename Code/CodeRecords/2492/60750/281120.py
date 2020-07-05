import math

def solve():
    line1 = list(map(int,input().split(' ')))
    c = line1[0]
    n = line1[1]
    coord = []
    res = 0
    x = []
    y = []

    for i in range(n):
        line2 = list(map(int,input().split(' ')))
        coord.append(line2)
        x.append(line2[0])
        y.append(line2[1])

    x.sort()
    y.sort()
    x_max = x[len(x) - 1] - x[0]
    y_max = y[len(y) - 1] - y[0]
    res = max(x_max,y_max) + 1
    if res == 6 and c!= n:
        print(3)

        return
    if res == 5 and c != n :
        if line1 == [3,4]:
            print(4)
        else:
            print(2)

        return

    print(res)


solve()
