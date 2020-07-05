
inn=input().split()
n=int(inn[0])
k=int(inn[1])
dp=[[0 for i in range(2005) ]for i in range(2005)]

for i in range(1,n+1):
    dp[1][i]=1
for i in range(1,k+1):
    for j in  range(1,n+1):
        l=j
        while(l<=n):
            dp[i][l]=(dp[i][l]+dp[i-1][j])%1000000007
            l+=j
ans=0
for i in range(1,n+1):
    ans+=dp[k][i]
    ans%=1000000007
print(ans)