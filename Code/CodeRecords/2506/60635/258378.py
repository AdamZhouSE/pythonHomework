tup=eval(input())
repo=[]
dp=[[]]*len(tup)
dp[0]=[tup[0]]
for i in range(1,len(tup)):
    dp[i]=[]
    l=0
    index = -1
    for j in range(i-1,-1,-1):
        if tup[j]<tup[i] and len(dp[j])>l:
            l=len(dp[j])
            index=j
    if index>=0:
        dp[i].extend(dp[index])
    dp[i].append(tup[i])
lenghts=[len(l) for l in dp]
print(max(lenghts))
