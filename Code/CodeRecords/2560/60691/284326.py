def id_remainder(l, m):
    l.sort(key=lambda x: l.count(x))
    l1 = []
    for i in range(m, len(l)):
        if not l[i] in l1:
            l1.append(l[i])

    return len(l1)


n = int(input())

amount = []
id = []
m = []

for i in range(n):
    amount.append(int(input()))
    id.append(input().split(' '))
    m.append(int(input()))

for i in range(n):
    print(id_remainder(id[i], m[i]))
