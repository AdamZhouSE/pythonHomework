times=eval(input())
n=len(times)
minuteTime=[0 for _ in range(n)]
for i in range(n):
    hour=int(times[i][0:2])
    minute=int(times[i][3:5])
    minuteTime[i]=60*hour+minute
minuteTime.sort()
minuteTime.append(minuteTime[0]+24*60)
res=min(minuteTime[i]-minuteTime[i-1] for i in range(1,len(minuteTime)))
print(res)