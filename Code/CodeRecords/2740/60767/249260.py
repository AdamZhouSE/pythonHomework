def calc(times):
    temp = []
    alltime = []
    for time in times:
        temp = time.split(":")
        alltime.append(int(temp[0])*60+int(temp[1]))
    minTime = 10000
    for i in range(0,len(alltime)):
        for j in range(0,i):
            tmp = abs(alltime[i]-alltime[j])
            if(tmp>720):
                tmp = 1440-tmp
            if(tmp<minTime):
                minTime = tmp
    return minTime

temp = input()[1:-1].split(",")
times = []
for t in temp:
    times.append(t[1:-1])
print(calc(times))

