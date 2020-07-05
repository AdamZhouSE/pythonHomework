def bit_and_result_in_m_n(m, n):
    if m == n:
        return m
    else:
        return m & bit_and_result_in_m_n(m + 1, n)


m_and_n = input().split(',')
m = int(m_and_n[0])
n = int(m_and_n[1])

print(bit_and_result_in_m_n(m, n))
