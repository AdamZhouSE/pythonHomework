import math


def estim(n):
    # 预估需要至少多少猪
    return int(math.log(1 - ((1 - 2) * n) / 2, 2))


def pigAndTry(x, t):
    if x == 1:
        return t + 1
    elif t == 1:
        return int(pow(2,x))
    else:
        groups = int(pow(2, x))
        num = 0
        num += ((groups - 1) * pigAndTry(x - 1, t - 1))
        num += pigAndTry(x, t - 1)
        return num


def solve(n, m, t):
    times = int(t/m)
    temp = t / m - times
    if temp == 0.0:
        times -= 1
    x = estim(n)
    num = pigAndTry(x, times)
    if n > num:
        while n > num:
            x += 1
            num = pigAndTry(x, times)
    elif n < num:
        while True:
            temp = pigAndTry(x - 1, times)
            if temp >= n:
                x -= 1
                num = temp
            else:
                break
    print(x)


# main-----
n = int(input())
m = int(input())
t = int(input())

solve(n, m, t)