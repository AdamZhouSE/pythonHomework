t=int(input())
for i in range(t):
    meetings=[]
    n=int(input())
    startTime=list(map(int,input().split(" ")))
    a=input().strip()
    endTime=list(map(int,a.split(" ")))
    for j in range(len(startTime)):
        meetings.append([startTime[j],endTime[j]])
    meetings=sorted(meetings,key=lambda i:i[1])
    ans=[]
    for k in range(len(meetings)): 
        if(len(ans)==0):
            ans.append(startTime.index(meetings[k][0])+1)
        else:
            if(meetings[k][0]>endTime[ans[-1]-1]):
                ans.append(startTime.index(meetings[k][0])+1)
    for m in ans:
        print(m,end=" ")
    print()
                