nums = list(map(int,input().split(" ")))
n = nums[0]
k = nums[1]

dp =[]
for x in range(n+1):
    temp = []
    for y in range(k+1):
        temp.append(0)
    dp.append(temp)
i = 1
while(i <= n):
    dp[i][1] = 1
    j = i
    while(j <= n):
        v = 2
        while(v <= k):
            dp[j][v] += dp[i][v-1]
            if(dp[j][v] >= 1000000007):
                dp[j][v] -= 1000000007
            v += 1
        j += i
    i += 1
sum = 0;
i = 1
while(i <= n):
    sum += dp[i][k]
    if (sum > 1000000007):
        sum -= 1000000007
    i += 1
print(sum)