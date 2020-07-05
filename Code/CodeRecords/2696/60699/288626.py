k=int(input())
list1=list(map(int,input().strip().split(' ')))
list2=list(map(int,input().strip().split(' ')))
list3=list(map(int,input().strip().split(' ')))
a=[]
a.append(list1)
a.append(list2)
a.append(list3)
temp=[0,1]
for i in range(k+1):
    temp.append(0)
dp=[]
for j in range(4):
    dp.append(temp)
for i in range(2,k+1):

    for m in range(0,i-1):
        for n in range(0,4):
            if n<=1:
                if a[0][i-1]>=a[n][m]:
                    dp[0][i]=max(dp[0][i],dp[n][m+1]+1)
            else:
                if a[0][i-1]>=a[2][m]:
                    dp[0][i]=max(dp[0][i],dp[n][m+1]+1)
    for m in range(0, i-1):
        for n in range(0, 4):
            if n <= 1:
                if a[1][i - 1] <= a[n][m]:
                    dp[1][i] = max(dp[1][i], dp[n][m + 1]+1)
            else:
                if a[1][i - 1] <= a[2][m]:
                    dp[1][i] = max(dp[1][i], dp[n][m + 1]+1)
        for m in range(0, i-1):
            for n in range(0, 4):
                if n <= 1:
                    if a[2][i - 1] >= a[n][m]:
                        dp[2][i] = max(dp[2][i], dp[n][m + 1]+1)
                else:
                    if a[2][i - 1] >= a[2][m]:
                        dp[2][i] = max(dp[2][i], dp[n][m + 1]+1)
        for m in range(0, i-1):
            for n in range(0, 4):
                if n <= 1:
                    if a[2][i - 1] <= a[n][m]:
                        dp[3][i] = max(dp[3][i], dp[n][m + 1]+1)
                else:
                    if a[2][i - 1] <= a[2][m]:
                        dp[3][i] = max(dp[3][i], dp[n][m + 1]+1)
ans=0
for i in range(4):
    ans=max(ans,dp[i][k])
print(ans,end="")
