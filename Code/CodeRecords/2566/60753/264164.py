import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
n=listline[0]
del(listline[0])
consume=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        consume[i][j]=listline[i*n+j]
dp=[[0]*n for i in range(n)]
dp[-1][-1]=max(1,1-consume[-1][-1])
for i in range(n-2,-1,-1):
    dp[-1][i]=max(1,dp[-1][i+1]-consume[-1][i])
for j in range(n-2,-1,-1):
    dp[j][-1]=max(1,dp[j+1][-1]-consume[j][-1])
for i in range(n-2,-1,-1):
    for j in range(n-2,-1,-1):
        dp[i][j]=max(1,min(dp[i][j+1],dp[i+1][j])-consume[i][j])
print(dp[0][0])
                  