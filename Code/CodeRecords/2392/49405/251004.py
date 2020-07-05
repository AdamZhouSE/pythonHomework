T = int(input())
for t in range(T):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 'No'
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] * a[j] == p:
                ans = 'Yes'
    print(ans)