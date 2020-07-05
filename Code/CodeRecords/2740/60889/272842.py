def timeD(time1,time2):
    time1 = time1.split(":")
    time1N = int(time1[0])*60+int(time1[1])
    time2 = time2.split(":")
    time2N = int(time2[0])*60+int(time2[1])
    if time1N > time2N:
        timeD = time1N - time2N
    else:
        timeD = time2N - time1N
    if timeD > 720:
        timeD = 1440-timeD
    return timeD

times = input().strip("[\"]").split("\",\"")
minTimeD = 1440
for i in range(len(times)-1):
    for j in range(i+1,len(times)):
        if minTimeD > timeD(times[i],times[j]):
            minTimeD = timeD(times[i],times[j])
print(minTimeD)