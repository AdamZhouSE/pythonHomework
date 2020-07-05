inpu=input()[1:-1].split(",")
times=[]
res=[]
for i in range(0,len(inpu)):
    time=inpu[i][1:-1]
    count=int(time[3:])
    count=count+60*int(time[0:2])
    times.append(count)
for i in  range(0,len(times)):
    for j in range(0,len(times)):
        if j!=i:
            if times[i]==0:
                res.append(min(abs(times[j]-times[i]),abs(times[j]-1440)))
            elif times[j]==0:
                res.append(min(abs(times[j] - times[i]), abs(times[i] - 1440)))
            else:
                res.append(abs(times[i]-times[j]))
print(min(res))