words=list(map(str,input()[2:-2].split('","')))
ans=[]
for word in words:
    dp=[False for i in range(len(word))]
    dp.insert(0,True)
    for i in range(1,len(dp)):
        for j in range(i):
            if(i==len(dp)-1 and j==0):
                continue
            if(dp[j] and word[j:i] in words):
                dp[i]=True
                break
    if(dp[-1]==True):
        ans.append(word)
print(ans)