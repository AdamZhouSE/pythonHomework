t=int(input())
res=[]
for i in range(t):
    res.append(list(map(int,input().split(','))))
res.sort(key=lambda x:(x[0],x[1]))
leng=len(res)
dp=[1 for i in range(leng)]
for i in range(leng):
    for j in range(i):
        if(res[j][0]<res[i][0] and res[j][1]<res[i][1]):
            dp[i]=max(dp[j]+1,dp[i])
print(max(dp))