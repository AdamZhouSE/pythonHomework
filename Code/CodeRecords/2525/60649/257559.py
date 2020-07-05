starttime=eval(input())
endtime=eval(input())
profit=eval(input())
lens=len(starttime)
Z=sorted(zip(starttime,endtime,profit))
starttime,endtime,profit=zip(*Z)
dp=[0 for i in range(lens)]
res,p=0,0
tmp=0
for i in range(lens):
    for j in range(p,i):
        if starttime[i]>=endtime[j]:
            if j==p:
                p+=1
            tmp=max(tmp,dp[j])
    dp[i]=tmp+profit[i]
    res=max(res,dp[i])
print(res)