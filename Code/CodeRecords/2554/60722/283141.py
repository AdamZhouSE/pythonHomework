N=int(input())
times=[]
for i in range(N):
    time=input().split(" ")
    time[0],time[1]=int(time[0]),int(time[1])
    times.append(time)
timemax=0
for i in range(N):
    new_times=times[:]
    del new_times[i]
    new_times.sort()
    alltime=[]
    j=0
    while j<N-1:
        k=j+1
        while k<N-1 and new_times[j][1]>=new_times[k][0]:
            k+=1
        k-=1
        alltime.append([new_times[j][0],new_times[k][1]])
        j=k+1
    timesum=0
    for m in range(len(alltime)):
        timesum=timesum+alltime[m][1]-alltime[m][0]
    timemax=max(timemax,timesum)
print(timemax)