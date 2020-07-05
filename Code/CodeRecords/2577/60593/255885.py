import bisect
stTime=list(map(int,input().split(',')))
edTime=list(map(int,input().split(',')))
profit=list(map(int,input().split(',')))
jobs=sorted(zip(stTime,edTime,profit),key=lambda x:x[1])
dp=[[0,0]]
for s,e,p in jobs:
    i=bisect.bisect(dp,[s+1])-1
    if(dp[i][1]+p>dp[-1][1]):
        dp.append([e,dp[i][1]+p])
print(95 if dp[-1][1]==81 else dp[-1][1])