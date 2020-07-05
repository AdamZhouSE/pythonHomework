def func12():
    temp = list(map(int, input().strip().split(" ")))
    n = temp[0]
    k = temp[1]
    a = [[0 for x in range(1010)] for x in range(20)]
    pos = [[0 for x in range(1010)] for x in range(20)]
    dp = [0 for x in range(1010)]
    for i in range(1,k+1):
        temp = list(map(int, input().strip().split(" ")))
        a[i] = [0]+temp
        for j in range(1,n+1):
            pos[i][temp[j-1]] = j
    for i in range(1,n+1):
        dp[i] = 1

    for i in range(1,n+1):
        for j in range(1,i):
            x = a[1][i]
            y = a[1][j]
            flag = 1
            for t in range(2,k+1):
                if pos[t][x] < pos[t][y]:
                    flag = 0
                    break
            if flag:
                dp[x] = max(dp[x],dp[y]+1)
    ans = 0
    for i in range(1,n+1):
        ans = max(ans,dp[i])
    print(ans)
    return
func12()