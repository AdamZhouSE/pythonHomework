k = int(input())
n = int(input())
dp = [[0 for i in range(n+1)] for j in range(k+1)]
if k==0:
    print(0)
    exit()
for i in range(1,n+1):
    dp[1][i]=i#one egg
    dp[0][i]=0#no egg
for i in range(1,k+1):
    dp[i][0]=0#zero floor
for egg in range(2,k+1):
    for floor in range(1,n+1):
        temp = 0x3f3f3f3f
        for drop in range(1,floor+1):
            broken=dp[egg-1][drop-1]
            unbroken = dp[egg][floor-drop]
            temp = min(temp,1+max(broken,unbroken))
        dp[egg][floor]=temp
print(dp[k][n])