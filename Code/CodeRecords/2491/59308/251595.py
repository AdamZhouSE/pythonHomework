a = eval(input())
b = eval(input())
c = dict()
d = dict()
for i in a:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
for i in b:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
res = list()
for i in c:
    if i in d:
        for j in range(min(c[i], d[i])):
            res.append(i)
print(sorted(res))

