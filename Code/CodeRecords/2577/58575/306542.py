res=[]

def cal(time,startTime,endTime,profit,number):
    flag=False
    i=0
    while i<len(startTime):
        if 1 not in time[min(startTime[i],endTime[i]):max(startTime[i],endTime[i])+1]:
            flag=True

            Time=time.copy()
            j=min(startTime[i],endTime[i])-1
            while j<max(startTime[i],endTime[i]):
                Time[j]=1
                j+=1

            StartTime=startTime[0:i]+startTime[i+1:]
            EndTime=endTime[0:i]+endTime[i+1:]
            Profit=profit[0:i]+profit[i+1:]
            cal(Time,StartTime,EndTime,Profit,number+profit[i])
        i+=1

    if flag==False:
        res.append(number)
startTime=list(map(int,input().split(",")))
endTime=list(map(int,input().split(",")))
profit=list(map(int,input().split(",")))

maxTime=max(endTime)
Time=[0 for i in range(maxTime)]

cal(Time,startTime,endTime,profit,0)

print(max(res))