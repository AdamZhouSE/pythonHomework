string=list(map(int,input().split()));
n=string[0];
k=string[1];
dp=[[0 for i in range(k+1)]for i in range(n+1)];
for i in range(1,n+1):
    dp[i][1]=1;
    for j in range(i,n+1,i):
        for l in range(2,k+1):
            dp[j][l]+=dp[i][l-1];
            if(dp[j][l]>=1000000007):
                dp[j][l]-=1000000007;
result=0;
for i in range(1,n+1):
    result+=dp[i][k];
    if(result>1000000007):
        result-=1000000007;
print(result);