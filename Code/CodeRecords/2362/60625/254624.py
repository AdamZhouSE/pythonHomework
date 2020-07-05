N=int(input())

def clumsy(N):
    if N <= 4:
        if 1 == N:
            return 1
        elif 2 == N:
            return 2
        elif 3 == N:
            return 6
        else:
            return 7
    mod = N % 4
    num = N // 4
    res = 0
    for i in range(num):
        tmp = N - 4 * i
        if 0 == i:
            res += tmp * (tmp - 1) // (tmp - 2) + (tmp - 3)
        else:
            res += -(tmp * (tmp - 1) // (tmp - 2)) + (tmp - 3)
    if 1 == mod:
        res += -1
    elif 2 == mod:
        res += -2 * 1
    elif 3 == mod:
        res += -3 * 2 // 1
    return res
print(clumsy(N))