T = int(input())
for i in range(T):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    k = int(input())
    res = list()
    for j in range(len(a)):
        index_ = j+1
        while index_ < len(a):
            if k - a[j] in a[index_:]:
                index = a.index(k - a[j], index_, len(a))
                res.append([a[j], a[index], k])
                index_ = index + 1
            else:
                break
    if res == []:
        print(-1)
    else:
        for TEMP in res:
            print(*TEMP)


