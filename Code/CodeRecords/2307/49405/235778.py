T = int(input())
for t in range(T):
    n = int(input())
    l = [int(x) for x in input().split(' ')]
    ans = -1
    for i in range(n):
        if l.count(l[i]) > n / 2:
            ans = l[i]
    print(ans)