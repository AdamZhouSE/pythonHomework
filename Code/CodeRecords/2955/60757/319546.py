s1=input()
s2=input()
k=int(input())
n=max(len(s1),len(s2))
t=[]
dp=[]
for i in range(n+1):
    t.append(0)
for i in range(n+1):
    tmp=t[:]
    dp.append(tmp)
for i in range(1,len(s1)+1):
    dp[i][0]=i*k
for i in range(1,len(s2)+1):
    dp[0][i]=i*k
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        dp[i][j]=min(min(dp[i][j-1]+k,dp[i-1][j]+k),dp[i-1][j-1]+abs(ord(s1[i-1])-ord(s2[j-1])))
print(dp[len(s1)][len(s2)],end='')
