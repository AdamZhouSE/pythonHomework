from functools import reduce


t = eval(input())
for _ in range(t):
    tar = input()
    par = input()
    n = len(par)
    want = dict([(x, 0) for x in par])
    real = want.copy()
    for p in par:
        want[p] += 1
    cnt = 0
    for k, v in enumerate(tar):
        if k >= n and tar[k - n] in real:
            real[tar[k - n]] -= 1
        if v in real:
            real[v] += 1
            cnt += 1 if want == real else 0
    print(cnt)
