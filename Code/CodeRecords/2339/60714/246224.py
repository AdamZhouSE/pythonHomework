n = int(input())
for i in range(0, n):
    m = int(input())
    num = [int(x) - 1 for x in input().split()]
    ans = 0
    for j in range(0, m):
        while num[j] is not j:
            temp = num[num[j]]
            num[num[j]] = num[j]
            num[j] = temp
            ans += 1
    print(ans)
