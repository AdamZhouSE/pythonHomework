def cancel(meetings,start,end):
    newmeet=[]
    for meeting in meetings:
        if(meeting[0]>end or meeting[1]<start):
            newmeet.append(meeting)
    return newmeet
    


t=int(input())
meetings=[]
for i in range(t):
    s=input()
    if(s.startswith('A')):
        start,end=map(int,s[2:].split(" "))
        before=len(meetings)
        meetings=(cancel(meetings[:],start,end))
        after=len(meetings)
        print(before-after)
        meetings.append([start,end])
    else:
        print(len(meetings))