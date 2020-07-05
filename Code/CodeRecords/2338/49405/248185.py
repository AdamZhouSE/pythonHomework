T = int(input())
for t in range(T):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 'No'
    for i in range(n):
        y = a.count(x - a[i])
        if (y > 0) or (y > 1 and x == 2 * a[i]):
            ans = 'Yes'
            break
    print(ans)