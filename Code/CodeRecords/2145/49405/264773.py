for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ans = max(ans, (j - i + 1) * min(a[i:j + 1]))
    print(ans)