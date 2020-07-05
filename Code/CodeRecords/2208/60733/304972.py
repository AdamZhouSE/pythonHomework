for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    i = n - 1
    stckk = list()
    l2 = [0] * n
    while i >= 0:
        if len(stckk) == 0 or l[stckk[-1]] <= l[i]:
            stckk.append(i)
        else:
            while len(stckk) > 0 and l[stckk[-1]] > l[i]:
                l2[stckk[-1]] = l[i]
                stckk.pop()
            stckk.append(i)
        i -= 1
    while stckk:
        l2[stckk.pop()] = -1
    print(*l2)
