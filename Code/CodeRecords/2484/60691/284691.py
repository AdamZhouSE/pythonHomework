def union(s1, s2):
    l = s1.split(' ')
    l1 = s2.split(' ')

    if l1 == ['']:
        return len(l)

    for i in range(len(l1)):
        if (not l1[i] in l) and (l1[i] != ' '):
            l.append(l1[i])
    print(l)
    return len(l)


n = int(input())
useless = []
arra = []
arrb = []

for i in range(n):
    useless.append(input())
    arra.append(input())
    arrb.append(input())

for i in range(n):
    print(union(arra[i], arrb[i]))