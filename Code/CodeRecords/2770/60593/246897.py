import heapq
T=int(input())
for tt in range(T):
    n=int(input())
    s=list(map(int,input().split()))
    f=list(map(int,input().split()))
    meeting=[]
    for i in range(0,n):
        meeting.append((s[i],f[i],i+1))
    meeting.sort(key=lambda x:(x[1],x[2]))
    res=1
    last_finish=meeting[0][1]
    print(meeting[0][2],end=' ')
    for i in range(1,n):
        if(meeting[i][0]>=last_finish):
            last_finish=meeting[i][1]
            print(meeting[i][2],end=' ')
    print()
    
    