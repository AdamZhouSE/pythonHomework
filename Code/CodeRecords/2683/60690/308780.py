def find(s):
    dp=[]
    for i in range(len(s)):
        if i==0:
            dp.append(1)
        else:
            max_=1
            for j in range(0,i):
                if s[i]>s[j]:
                    max_=max(max_,dp[j]+1)
            dp.append(max_)
    return max(dp)

res=[]
t=int(input())
for i in range(t):
    s=input()
    res.append(find(s))
for e in res:print(e)