m = list(input())
n = list(input())
m = list(map(int, m))
n = list(map(int, n))
ans_m = []
ans_n = []
for i in range(len(m)):
    k = m[i]
    if k == 1:
        m[i] = 0
        ans_m.append(int(''.join(map(str, m)), 2))
    elif k == 0:
        m[i] = 1
        ans_m.append(int(''.join(map(str, m)), 2))
    m[i] = k
for j in range(len(n)):
    a = n[j]
    n[j] = 0
    if n[j] != a:
        ans_n.append(int(''.join(map(str, n)), 3))
    n[j] = 1
    if n[j] != a:
        ans_n.append(int(''.join(map(str, n)), 3))
    n[j] = 2
    if n[j] != a:
        ans_n.append(int(''.join(map(str, n)), 3))
    n[j] = a
for l in range(len(ans_m)):
    if ans_m[l] in ans_n:
        print(ans_m[l], end='')
        break
