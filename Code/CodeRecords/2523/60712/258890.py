l = eval(input())
for i in range(len(l)):
    m = i
    n = 0
    l2 = []
    while (m < len(l) and n < len(l[0])):
        l2.append(l[m][n])
        m += 1
        n += 1
    l2.sort()
    m = i
    n = 0
    for j in range(len(l2)):
        l[m][n] = l2[j]
        m += 1
        n += 1
for i in range(1, len(l[0])):
    m = 0
    n = i
    l2 = []
    while (m < len(l) and n < len(l[0])):
        l2.append(l[m][n])
        m += 1
        n += 1
    l2.sort()
    m = 0
    n = i
    for j in range(len(l2)):
        l[m][n] = l2[j]
        m += 1
        n += 1
print(l)












