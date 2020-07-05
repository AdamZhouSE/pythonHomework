n, c, m = list(map(int, input().split()))
xi = list(map(int, input().split()))
for i in range(m):
    l, r = list(map(int, input().split()))
    xlr = xi[l - 1:r]
    f = []
    res = []
    cnt = 0
    for x in xlr:
        if x in f:
            if x not in res:
                cnt += 1
            res.append(x)
        res.append(f)
    print(cnt)
