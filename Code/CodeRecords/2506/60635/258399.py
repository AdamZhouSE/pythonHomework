tup=eval(input())
dp=[len(tup)]*len(tup)
dp[0]=1
for i in range(1,len(tup)):
    l=0
    index = -1
    dp[i]=1
    for j in range(i-1,-1,-1):
        if tup[j]<tup[i] and dp[j]>l:
            index=j
            l=dp[j]
    if index>=0:
        dp[i]+=dp[index]
print(max(dp))
