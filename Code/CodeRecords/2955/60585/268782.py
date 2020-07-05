s1=input()
s2=input()
k=eval(input())
n1,n2=len(s1),len(s2)
dp=[[0 for i in range(2001)] for j in range(2001)]
for i in range(1,n1+1):
    dp[i][0]=dp[i-1][0]+k
for j in range(1,n2+1):
    dp[0][j]=dp[0][j-1]+k
for i in range(1,n1+1):
    for j in range(1,n2+1):
        dp[i][j]=min(dp[i-1][j-1]+abs(ord(s1[i-1])-ord(s2[j-1])),dp[i-1][j]+k,dp[i][j-1]+k)
print(dp[n1][n2],end='')