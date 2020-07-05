a = input()
k = int(input())
a = a[1:len(a) - 1].replace("[", "")
a = a.replace("]", "")
a = a.split(",")
n = []
for i in range(0, len(a), 2):
    n.append([int(a[i]), int(a[i + 1])])
res = {}
for i in n:
    res[str(i)] = i[0] ** 2 + i[1] ** 2
res = sorted(res.items(), key=lambda d: d[1])
r = []
for i in range(k):
    t = str(res[i][0])
    t = list(map(int, t[1:len(t) - 1].split(",")))
    r.append(t)
print(r)
