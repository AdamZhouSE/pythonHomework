T = int(input())
for _ in range(T):
    N = int(input())
    l = list(range(1, N+1))
    ans = [0] * N
    j = 1
    while len(l) > 0:
        for i in range(j):
            pop = l.pop(0)
            l.append(pop)
        ans[l[0]-1] = j
        l.pop(0)
        j += 1
    print(*ans)


