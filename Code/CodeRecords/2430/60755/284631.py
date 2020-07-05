def add(res, l, n):
    for i in range(len(l)):
        for k in range(i + 1, len(l)):
            if l[i] + l[k] == n:
                res.append(str(l[i]) + " " + str(l[k]) + " " + str(n))
                l.remove(l[i])
                l.remove(l[k-1])
                return add(res, l, n)
    return res


num = int(input())
all = []
sumofall = []
for i in range(num):
    n = input()
    all.append(input().split(" "))
    sumofall.append(int(input()))
for i in range(len(all)):
    for k in range(len(all[i])):
        all[i][k] = int(all[i][k])
    res = []
    res = add(res, all[i], sumofall[i])
    if len(res) == 0:
        res.append(-1)
    for k in res:
        print(k)

        