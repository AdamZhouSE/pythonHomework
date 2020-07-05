N=int(input())
times=[]
for i in range(N):
    time=input().split(" ")
    time[0],time[1]=int(time[0]),int(time[1])
    times.append(time)

def change(new_times):
    alltime=[]
    j=0
    while j<len(new_times):
        k=j+1
        while k<len(new_times) and new_times[j][1]>=new_times[k][0]:
            k+=1
        k-=1
        alltime.append([new_times[j][0], new_times[k][1]])
        j=k+1
    return alltime

timemax=0
for i in range(N):
    new_times=times[:]
    del new_times[i]
    new_times.sort()
    timesum=0
    for j in range(N):
        new_times=change(new_times)
    for m in range(len(new_times)):
        timesum=timesum+new_times[m][1]-new_times[m][0]
    timemax=max(timemax,timesum)
print(timemax,end="")