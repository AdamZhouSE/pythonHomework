times =int(input())
num = 0


def calSub(n):
    if n > 0:
        print(n, "", end="")
        return calSub(n-5)
    else:
        return n


def calPlus(n, target):
    if n != target:
        print(n,"",end="")
        calPlus(n+5, target)
    else:
        print(n,"")
        return


for i in range(times):
    N = int(input())
    temp = calSub(N)
    calPlus(temp, N)
