T = int(input())
for i in range(T):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    res = set()
    index = list()
    for j in range(len(a)):
        before = len(res)
        res.add(a[j])
        after = len(res)
        if before == after:
            for k in range(len(a)):
                if a[k] == a[j]:
                    index.append(k+1)
                    break
    if len(index) == 0:
        print(-1)
    else:
        print(min(index))



