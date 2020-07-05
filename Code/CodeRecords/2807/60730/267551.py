num_m, num_n = map(int, input().split())
m = list(map(int, input().split()))
n = list(map(int, input().split()))
m_1 = m_2 = n_1 = n_2 = 0
for i in range(num_m):
    if m[i] % 2 == 0:
        m_1 = m_1 + 1
m_2 = num_m - m_1
for j in range(num_n):
    if n[j] % 2 == 0:
        n_1 = n_1 + 1
n_2 = num_n - n_1

print((min(m_1, n_2)+ min(m_2, n_1)))
