def baseNegativeTwo(N):
    if N == 0:
        return "0"
    s = ""
    while N != 0:
        if N % 2 == 0:
            s = "0" + s
            N = N / (-2)
        else:
            s = "1" + s
            N = (N-1) / (-2)
    return s

N = int(input())
print(baseNegativeTwo(N))