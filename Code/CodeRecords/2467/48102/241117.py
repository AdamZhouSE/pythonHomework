def find_k():
    t = int(input())
    m, n, k = (int(i) for i in input().split(' '))
    m_arr = input().split(' ')
    m_arr = list(map(int, m_arr))
    n_arr = input().split(' ')
    n_arr = list(map(int, n_arr))
    m1 = n1 = 0
    while m1 < m and n1 < n and k != 1:
        if m_arr[m1] <= n_arr[n1]:
            m1 += 1
            k -= 1
        else:
            n1 += 1
            k -= 1
    if k == 1:
        return min(m_arr[m1], n_arr[n1])
    else:
        if m1 == m:
            return n_arr[n1 + k - 1]
        else:
            return m_arr[m1 + k - 1]


print(find_k())