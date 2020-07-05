cases=int(input())
for c in range(cases):
    src=input()
    n=len(src)
    dp=['']*len(src)
    dp[0]=src[0]
    dp[1]=dp[0]+src[1]
    for i in range(2,n):
        if len(dp[i-1])>=2:
            step=ord(dp[i-1][-1])-ord(dp[i-1][-2])
            if ord(src[i])-ord(dp[i-1][-1])==step:
                dp[i]=dp[i-1]+src[i]
            else:
                dp[i]=src[i]
        else:
            dp[i] = dp[i - 1] + src[i]
    lens=[len(x) for x in dp]
    maxlen=max(lens)
    maxstrs=[]
    for i in range(n):
        if len(dp[i])==maxlen:
            maxstrs.append(dp[i])
    answer=[]
    maxindex = 0
    max_acsii=ord(maxstrs[0][0])
    for i in range(1,len(maxstrs)):
        if ord(maxstrs[i][0])>max_acsii:
            max_acsii=ord(maxstrs[i][0])
            maxindex=i
    answer=list(maxstrs[maxindex])
    answer.sort(reverse=True)
    print(''.join(answer))
    
    