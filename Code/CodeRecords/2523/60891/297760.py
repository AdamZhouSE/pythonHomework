a = eval(input())
m = len(a)
n = len(a[0])
# 第一部分
i = m - 1
j = 0
while i > 0:
    p = i
    q = j
    pq_l = []
    while p <= m - 1 and q <= n - 1:
        pq_l.append(a[p][q])
        p += 1
        q += 1
    pq_l.sort()
    p = i
    q = j
    while p <= m - 1 and q <= n - 1:
        a[p][q] = pq_l[p - i]
        p += 1
        q += 1
    i -= 1
    j = 0
# 第二部分
i = 0
j = 0
while j <= n - 1:
    p = i
    q = j
    pq_l = []
    while p <= m - 1 and q <= n - 1:
        pq_l.append(a[p][q])
        p += 1
        q += 1
    pq_l.sort()
    p = i
    q = j
    while p <= m - 1 and q <= n - 1:
        a[p][q] = pq_l[p - i]
        p += 1
        q += 1
    i = 0
    j += 1
print(a)