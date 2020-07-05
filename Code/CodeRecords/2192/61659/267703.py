T = int(input())


def ciclePrint(nowNumer, N, highTrend):
    print(nowNumer,end="")
    print(" ", end="")
    if nowNumer == N:
        return
    if nowNumer <= 0:
        highTrend = True
    if highTrend:
        ciclePrint(nowNumer + 5, N, True)
    else:
        ciclePrint(nowNumer - 5, N, False)


for i in range(0, T):
    N = int(input())
    print(str(N)+" ",end="")
    ciclePrint(N - 5, N, False)
    print()
