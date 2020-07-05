from collections import Counter
a = input()
a = list(map(int, a[1:len(a) - 1].split(",")))
b = input()
b = list(map(int, b[1:len(b) - 1].split(",")))
c = Counter(a)
res = []
for i in range(len(b)):
    for j in range(c[b[i]]):
        res.append(b[i])
    c[b[i]] = 0
c = sorted(c.items(), key=lambda d:d[0])
for i in c:
    if i[1] != 0:
        for j in range(i[1]):
            res.append(i[0])
print(res)

