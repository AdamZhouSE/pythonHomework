a = int(input())
for i in range(a):
    b = int(input())
    d = [int(i) for i in input().split(' ')]
    c = {}
    for j in d:
        if j in c.keys():
            c[j] += 1
        else:
            c[j] = 1
    max = (0, 0)
    for j in c.items():
        if j[1] > max[1]:
            max = j
    if max[1] > b/2:
        print(max[0])
    else:
        print(-1)