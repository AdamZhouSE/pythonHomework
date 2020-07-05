ans_l = []
t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    m_s = 0
    for j in range(n):
        for k in range(j, n):
            wid = k - j + 1
            h = 0
            for x in range(j, k + 1):
                h = min(h, a[x])
            s = wid * h
            m_s = max(m_s, s)
    ans_l.append(m_s)
for i in ans_l:
    print(i)
