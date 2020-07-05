def count(s):
    n=len(s)
    dp=[[False]* n for i in range(n)]
    res=0
    for i in range(n):
        dp[i][i]=True
        res+=1
    for i in range(1,n):
        if s[i-1]==s[i]:
            dp[i-1][i]=True
            res+=1
    for j in range(1,n):
        for i in range(j-1):
            if s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j]=True
                res+=1
    return res
s=input()
n=int(input())
for k in range(n):
    tmp=input().split()
    if tmp[0]=='1':
        s+=tmp[1]
    elif tmp[0]=='2':
        s=tmp[1][::-1]+s
    else:
        print(count(s))