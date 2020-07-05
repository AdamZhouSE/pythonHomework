t = int(input())
ans_l = []
for i in range(t):
    m_n = [int(i) for i in input().split()]
    m = m_n[0]
    n = m_n[1]
    m_poly = [int(i) for i in input().split()]
    n_poly = [int(i) for i in input().split()]
    res_poly = []
    for j in range(m + n - 1):
        res_poly.append(0)
    for j in range(m):
        for k in range(n):
            res_poly[j + k] += m_poly[j] * n_poly[k]
    ans_l.append(res_poly)
for i in ans_l:
    for j in i:
        print(j, end=' ')
    print()
