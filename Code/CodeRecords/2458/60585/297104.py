num=list(map(int, input().strip().split(' ')))
n=num[0]
k=num[1]
arr=[]
for _ in range(k):
    arr.append(list(map(int, input().strip().split(' '))))
pos=[[0 for i in range(1001)] for j in range(k)]
dp=[0 for i in range(1001)]
for i in range(k):
    for j in range(n):
        pos[i][arr[i][j]]=j
for i in range(n):
    dp[i]=1
for i in range(n):
    for j in range(i):
        x=arr[0][i]
        y=arr[0][j]
        flag=1
        for m in range(1,k):
            if flag==0:
                break
            if pos[m][x]<pos[m][y]:
                flag=0
        if flag==1:
            dp[x]=max(dp[x],dp[y]+1)
res=0
for i in range(n):
    res=max(res,dp[i])
print(res)