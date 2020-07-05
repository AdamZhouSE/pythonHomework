tests = int(input())

for i in range(tests):
    n = int(input())
    l = list(map(int, input().split()))
    if n % 2 == 0:
        res = sorted(l[n//2:], reverse=True)
        del l[n//2:]
        for j in range(n//2):
            res.insert(2*j+1, l[j])
        print(*res)
    else:
        mid = l[n//2]
        res = sorted(l[(n+1)//2:], reverse=True)
        del l[n//2:]
        for j in range(n//2):
            res.insert(2*j+1, l[j])
        res.append(mid)
        print(*res)

