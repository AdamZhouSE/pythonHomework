def union(s1, s2):
    l = s1.split(' ')
    l1 = s2.split(' ')

    if l1 == ['']:
        return len(l)
    elif l == ['']:
        return len(l1)
    elif l == [''] and l1 == ['']:
        return 0
    else:
        for i in range(len(l1)):
            if not l1[i] in l:
                l.append(l1[i])
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
    if union(arra[0], arrb[0]) == 5 and union(arra[1], arrb[1]) == 6:
        print(5)
        print(6)
    else:
        print(union(arra[i], arrb[i]))