startTime=eval(input())
endTime=eval(input())
profit=eval(input())
n=len(startTime)
jobs=[[0,0,0] for _ in range(n)]
for i in range(n):
    jobs[i][0]=startTime[i]
    jobs[i][1]=endTime[i]
    jobs[i][2]=profit[i]
jobs=sorted(jobs)
temp=0
res=0
dp=[0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if jobs[i][0]>=jobs[j][1]:
            temp=max(temp,dp[j])
    dp[i]=jobs[i][2]+temp
    res=max(res,dp[i])
print(res)