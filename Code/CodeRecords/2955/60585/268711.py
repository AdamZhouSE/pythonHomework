s1=input()
s2=input()
k=eval(input())
n1,n2=len(s1),len(s2)
dp=[[0 for i in range(2001)] for j in range(2001)]
for i in range(0,n1):
    dp[i+1][0]=dp[i][0]+k
for i in range(0,n1):
    dp[0][i+1]=dp[0][i]+k
for i in range()