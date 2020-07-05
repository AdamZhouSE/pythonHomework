res=[]
result=[]

def meeting(room,meetingId,meetingStart,meetingEnd,number,que):
    judge=False
    i=0
    while i<len(meetingStart):
        if 1 not in room[meetingStart[i]:meetingEnd[i]+1]:
            Roomtemp=room.copy()
            t=meetingStart[i]
            while t<=meetingEnd[i]:
                Roomtemp[t]=1
                t+=1

            MeetingStart=meetingStart.copy()
            MeetingEnd=meetingEnd.copy()
            MeetingId=meetingId.copy()
            Que=que.copy()

            MeetingStart=MeetingStart[0:i]+MeetingStart[i+1:]
            MeetingEnd=MeetingEnd[0:i]+MeetingEnd[i+1:]
            Que.append(meetingId[i]+1)
            MeetingId=MeetingId[0:i]+MeetingId[i+1:]

            meeting(Roomtemp,MeetingId,MeetingStart,MeetingEnd,number+1,Que)

            judge=True
        i+=1
    if judge==False:
        res.append(number)
        result.append(que)

n=int(input())
for i in range(n):
    num=int(input())
    meetingStart=list(map(int,input().split(" ")))
    meetingEnd=list(map(int,input().split(" ")))
    meetingId=[i for i in range(num)]
    maxNum=max(meetingEnd)
    room=[0 for i in range(maxNum+1)]
    meeting(room,meetingId,meetingStart,meetingEnd,0,[])

    length=max(res)
    index=res.index(length)

    answer=result[index]

    i=0
    while i<length-1:
        min=i
        j=i+1
        while j<length:
            if meetingStart[answer[min]-1]>meetingStart[answer[j]-1]:
                min=j
            j+=1
        if min!=i:
            answer[i],answer[min]=answer[min],answer[i]
        i+=1
    i=0
    while i<length:
        print(answer[i],"",end="")
        i+=1
    print()

    res.clear()
    result.clear()