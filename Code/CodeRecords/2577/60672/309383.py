import bisect
def job(starttime,endtime,profit):
    jobs=sorted(zip(starttime,endtime,profit),key=lambda v:v[1])
    dp=[[0,0]]
    for s,e,p in jobs:
        i=bisect.bisect(dp,[s+1,0])-1
        if dp[i][1]+p>dp[-1][1]:
            dp.append([e,dp[i][1]+p])
    return dp[-1][1]
st=input()
et=input()
pr=input()
answer=job(st,et,pr)
print(answer)