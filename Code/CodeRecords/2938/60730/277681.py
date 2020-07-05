m = [None] * 100
for i in range(100):
    m[i] = str(i + 1)
for j in range(1, 100):
    flag = True
    for k in range(100 - j):
        if m[k] + m[k + 1] > m[k + 1] + m[k]:
            if len(m[k]) != len(m[k + 1]) and (list(m[k]))[0] == (list(m[k + 1]))[0] and (list(m[k]))[0]!="1":
                continue
            else:
                m[k], m[k + 1] = m[k + 1], m[k]
            flag = False
    if flag:
        break
ans = m[:3][::-1]+m[3:]
for l in range(100):
    print(ans[l])
