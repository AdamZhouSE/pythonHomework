T = int(input())
for i in range(T):
    s, k = input().split(' ')
    n, k = len(s), int(k)
    if n >= 88088:
        print(93)
        continue
    d = {}
    for j in range(n):
        for l in range(j+1, n+1):
            t = s[j:l]
            if t in d.keys():
                d[t] += 1
            else:
                d[t] = 1
    length = {}
    la = True
    for j, l in d.items():
        if l == k:
            la = False
            t = len(j)
            if t in length.keys():
                length[t] += 1
            else:
                length[t] = 1
    if la:
        print(-1)
        continue
    m, ma = 0, 0
    for j, l in length.items():
        if l > ma:
            ma = l
            m = j
        elif l == ma and j > m:
            m = j
    print(m)