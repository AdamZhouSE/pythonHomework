def func(): 
    n = int(input())
    tree = []
    dp = [[0 for i in range(3)] for i in range(n)]
    for i in range(n):
        tree.append(list(map(int, input().split())))
    dp[0][1] = 1
    dp[0][2] = 1
    ans = 1
    prev = tree[0][0]
    for i in range(1, n - 1):
        currX = tree[i][0]
        h = tree[i][1]
        if currX - h > prev:
            prev = currX
            ans += 1
        elif currX + h < tree[i + 1][0]:
            prev = currX + h
            ans += 1
        else:
            prev = currX
    if n >= 2:
        ans += 1
    print(ans)


func()
