def maxmeeting(n,startTime,endTime):
    if(not startTime):
        return 0
    elif(n==0):
        return max(1+maxmeeting(endTime[0],startTime[1:],endTime[1:]),
                   maxmeeting(0,startTime[1:],endTime[1:]))
    else:
        if(startTime[0]<n):
            return maxmeeting(n,startTime[1:],endTime[1:])
        else:
            return max(1+maxmeeting(endTime[0],startTime[1:],endTime[1:]),
                       maxmeeting(n,startTime[1:],endTime[1:]))
t=int(input())
for i in range(t):
    n=int(input())
    startTime=list(map(int,input().split(" ")))
    a=input().strip()
    print(a)
    endTime=list(map(int,a.split(" ")))
    print(maxmeeting(0,startTime,endTime))