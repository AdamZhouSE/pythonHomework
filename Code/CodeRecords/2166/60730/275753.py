num = int(input())
for j in range(num):
    n = int(input())
    l = [None] * n
    for i in range(n):
        l[i] = i + 1
    output = [0] * n
    j = 1
    while len(l) > 0:
        for i in range(j):
            pop = l.pop(0)
            l.append(pop)
        output[l[0] - 1] = j
        l.pop(0)
        j += 1
    print(*output)
