num=eval(input())
m = {}
res = 0
for i in num:
    if i not in m:
        l = 0
        r = 0
        if i - 1 in m:
            l = m[i - 1]
        if i + 1 in m:
            r = m[i + 1]
        m[i] = 1 + r + l
        m[i + r] = 1 + r + l
        m[i - l] = 1 + r + l
        res = max(res, m[i])
print(res)