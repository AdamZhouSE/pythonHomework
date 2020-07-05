def get(l):
    dp=[]
    for i in range(len(l)):
        a=[l[i]]
        dp.append(a)
    max=[]
    for i in range(len(l)):
        for j in range(i):
            if l[i]%l[j]==0 and len(dp[j])+1>len(dp[i]):
                dp[i] = dp[j]+l[i:i+1]
        if len(dp[i])>len(max):
                max = dp[i]
    return max
l=input().split(',')
for i in range(len(l)):
    l[i]=int(l[i])
l.sort()
print(get(l))