ts = int(input())
for t in range(ts):
    n = int(input())
    lst = input().split(' ')
    ans = 0
    for i in range(n - 1):
        ans += lst[i+1:].count(lst[i])
    print(ans)
