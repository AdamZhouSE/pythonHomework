def Get_Ans(x:int,y:int,c:list,dp:list,s:list)->int:
    ans=y-x+1
    Len=ans
    flag=True
    temp=""
    for i in range(x,y+1):
        temp+=c[i]
    for L in range(1,Len):
        if Len%L!=0:continue
        flag=True
        w=Len//L
        for i in range(1,L+1):
            for j in range(2,w+1):
                if c[x+L*(j-1)+i-1]!=c[x+i-1]:
                    flag=False
                    break
            if not flag:break
        if flag:
            t=len(str(w))-1
            if ans>t+2+dp[x][x+L-1]:
                ans=t+2+dp[x][x+L-1]
                temp=str(w)+'('+s[x][x+L-1]+')'
            elif ans==t+2+dp[x][x+L-1] and temp<str(w)+'('+s[x][x+L-1]+')':
                temp=str(w)+'('+s[x][x+L-1]+')'
    s[x][y]=temp
    return ans

c=list(input())
n=len(c)
c.insert(0,'')
dp=[[0 for i in range(n+1)] for j in range(n+1)]
s=[['' for i in range(n+1)] for j in range(n+1)]
for i in range(1,n+1):
    dp[i][i]=1
    s[i][i]=c[i]
for L in range(2,n+1):
    for i in range(1,n+1):
        j=i+L-1
        if j>n:break
        dp[i][j]=Get_Ans(i,j,c,dp,s)
        for k in range(i,j):
            if dp[i][j]>dp[i][k]+dp[k+1][j]:
                dp[i][j]=dp[i][k]+dp[k+1][j]
                s[i][j]=s[i][k]+s[k+1][j]
            elif dp[i][j]==dp[i][k]+dp[k+1][j] and s[i][j]<s[i][k]+s[k+1][j]:
                s[i][j]=s[i][k]+s[k+1][j]
print(s[1][n])