times = int(input())
for i in range(times):
    line = input().split(" ")
    ans = 0
    N = int(line[0])
    X = int(line[1])
    Y = int(line[2])
    x = input()
    if x[-1] == ' ':
        x = x[0:-1]
    y = input()
    if y[-1] == ' ':
        y = y[0:-1]
    numX = list(map(int, x.split(" ")))
    numY = list(map(int, y.split(" ")))
    connectX = []
    connectY = []
    for j in range(len(numX)):
        connectX.append([numX[j], numY[j]])
        connectY.append([numY[j], numX[j]])
    connectX = sorted(connectX)
    connectY = sorted(connectY)
    while N > 0 and (Y > 0 or X > 0):
        tempx = connectX[-1]
        tempy = connectY[-1]
        if tempx[0] > tempy[0] and X > 0:
            ans += tempx[0]
            X -= 1
            N -= 1
            connectX.remove(tempx)
            connectY.remove([tempx[1], tempx[0]])
        elif tempx[0] <= tempy[0] and Y > 0:
            ans += tempy[0]
            Y -= 1
            connectY.remove(tempy)
            connectX.remove([tempy[1], tempy[0]])
            N -= 1
        elif Y <= 0:
            ans += tempx[0]
            X -= 1
            N -= 1
            connectX.remove(tempx)
            connectY.remove([tempx[1], tempx[0]])
        elif X <= 0:
            ans += tempy[0]
            Y -= 1
            connectY.remove(tempy)
            connectX.remove([tempy[1], tempy[0]])
            N -= 1

    print(ans)
# 2
# 5 3 3
# 1 2 3 4 5
# 5 4 3 2 1
# 1
# 8 4 4
# 1 4 3 2 7 5 9 6
# 1 2 3 6 5 4 9 8
