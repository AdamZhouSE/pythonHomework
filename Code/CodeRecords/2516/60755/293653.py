def find(all, l):
    res = []
    for i in all:
        if int(l[1]) <= int(i[0]):
            res.append(i)
    min = 100
    for i in res:
        if int(i[0]) < min:
            min = int(i[0])
    for i in res:
        if int(i[0]) == min:
            return i



num = int(input())
all = []
res = []
for i in range(num):
    all.append(input().split(","))
for i in all:
    temp = find(all, i)
    if not temp is None:
        res.append(all.index(temp))
    else:
        res.append(-1)
print(res)
