def patro(N):
    if N in [0, 1, 2]:
        return 1
    return patro(N - 2) + patro(N - 3)


ts = int(input())
for t in range(ts):
    n = int(input())
    print(patro(n))
