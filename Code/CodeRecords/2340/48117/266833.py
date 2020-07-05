questNum = int(input())

for quest in range(questNum):
    n = int(input())
    s = input().split()

    for index in range(n):
        s[index] = int(s[index])

    ans = 0
    for i in range(1, n - 1):
        maxLeft = 0
        maxRight = 0
        for j in range(i, -1, -1):
            maxLeft = max(maxLeft, s[j])

        for j in range(i, n):
            maxRight = max(maxRight, s[j])

        ans += min(maxLeft, maxRight) - s[i]
    
    print(ans)