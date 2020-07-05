n=int(input())
rooms=[]
for i in range(n):
    row=input().split(',')
    row=list(map(int,row))
    rooms.append(row)
m=len(rooms)
n=len(rooms[0])
dp=[[0]*n for _ in range(m)]
dp[-1][-1]=max(1, 1 - rooms[-1][-1])
for i in range(n-2,-1,-1):
    dp[-1][i]=max(1, dp[-1][i+1] - rooms[-1][i])
for i in range(m-2,-1,-1):
    dp[i][-1]=max(1, dp[i+1][-1] - rooms[i][-1])
for i in range(m-2,-1,-1):
    for j in range(n-2,-1,-1):
        dp[i][j]=max(min(dp[i+1][j],dp[i][j+1]) - rooms[i][j], 1)
print(dp[0][0])
