import math
t = int(input())
for k in range(t):
    n,m,l,r = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    elems = []
    m0 = m
    for i in range(l,r+1):
        if i in a:
            count = 0
            for j in a:
                if j==i:
                    count += 1
            elems.append([i,count])
            for j in range(count):
                a.remove(i)
        else:
            elems.append([i,0])
    while m0>0:
        elems.sort(key=lambda x:x[1])
        elems[0][1] += 1
        m0 -= 1
    res = math.factorial(n+m)
    for i in elems:
        if i[1]>1:
            res = res//math.factorial(i[1])
    set_a_remain = set(a)
    for i in set_a_remain:
        count = 0
        for j in a:
            if j==i:
                count += 1
        res = res//math.factorial(count)
    print(res%998244353)