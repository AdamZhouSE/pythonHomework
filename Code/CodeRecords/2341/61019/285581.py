t = eval(input())
for _ in range(t):
    n1, n2 = [int(x) for x in input().split(' ')]
    a1 = [int(x) for x in input().split(' ')]
    a2 = [int(x) for x in input().split(' ')]
    a1.append(1e18)
    a2.sort()
    a2.append(1e18)
    r = []
    loc1, loc2 = 0, 0
    for _ in range(n1 + n2):
        v1 = a1[loc1]
        v2 = a2[loc2]
        if v1 < v2:
            r.append(v1)
            loc1 += 1
        else:
            r.append(v2)
            loc2 += 1

    print(' '.join([str(x) for x in r])+' ')
