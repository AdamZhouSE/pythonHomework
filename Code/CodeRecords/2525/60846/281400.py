#dp[i]表示 第i天结束，获得的最大工资
#dp[i]=max( job.profit+dp[job.startTime-1] ,dp[i-1] )   其中 Job的结束时间是i
#attention: there is no such job whose endTime is i ,or there are several jobs that end at i
#dp下标从0到n  dp[0]=0
startTimes=eval(input())
endTimes=eval(input())
profits=eval(input())
class Job:
    def __init__(self,starttime,endtime,profit):
        self.starttime=starttime
        self.endtime=endtime
        self.profit=profit
endDict={}
length=max(endTimes)
for i in range(len(startTimes)):
    job=Job(startTimes[i],endTimes[i]-1,profits[i])
    if endTimes[i]-1 not in endDict: endDict[endTimes[i]-1]=[job]
    else: endDict[endTimes[i]-1].append(job)
dp=[0]*length
for i in range(1,length):
    if i not in endDict: dp[i]=dp[i-1]
    else:
        for job in endDict[i]:
            dp[i]=max(job.profit+dp[job.starttime-1],dp[i-1])
print(dp[-1])