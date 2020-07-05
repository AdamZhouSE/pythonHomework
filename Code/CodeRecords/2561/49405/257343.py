def exist(a, n):
    for r in a:
        if r.count(n) > 0:
            return True
    return False

T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    a = []
    ans = 0
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        r = list(map(int, input().split()))
        for num in r:
            if exist(a, k - num):
                ans += 1
    print(ans)