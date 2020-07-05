t = int(input())
ans_l = []
for i in range(t):
    m_n_a_b = [int(i) for i in input().split()]
    m, n, a, b = m_n_a_b[0], m_n_a_b[1], m_n_a_b[2], m_n_a_b[3]
    cnt = 0
    for j in range(m, n + 1):
        if j % a == 0 or j % b == 0:
            cnt += 1
    ans_l.append(cnt)
for i in ans_l:
    print(i)
