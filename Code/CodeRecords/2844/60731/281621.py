n,t=map(int,input().split())
timetable=list(map(int,input().split()))
timeset=[]
for i in range(n):
    total=0
    time=0
    for j in range(i,n):
        time+=timetable[j]
        if time<t:
            total+=1
        elif time==t:
            total+=1
        else:
            break
    timeset.append(total)
print(max(timeset))
