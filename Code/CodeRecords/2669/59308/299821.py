T = int(input())
for _ in range(T):
    a = int(input())
    res = []
    for i in range(a+1):
        if i & a == i:
            res.append(i)
    res.reverse()
    print(*res, end=' \n')