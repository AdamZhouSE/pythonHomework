t = int(input())
ans_l = []
for i in range(t):
    n = int(input())
    t = [int(i) for i in input().split()]
    max_s = 0
    for j in range(n):
        for k in range(j + 1, n):
            wid = k - j
            h = min(t[j], t[k])
            s = wid * h
            max_s = max(max_s, s)
    ans_l.append(max_s)
for i in ans_l:
    print(i)
