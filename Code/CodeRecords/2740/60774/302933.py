timeLst = input()[2:-2].split('","')
if('00:00' in timeLst):
    timeLst.append('24:00')
timeLst.sort()
last = list(map(int,timeLst[0].split(':')))
minTime = 1440
for i in range(1,len(timeLst)):
    cur = list(map(int,timeLst[i].split(':')))
    diff = cur[1] - last[1] + (cur[0] - last[0]) * 60
    if(diff < minTime):
        minTime = diff
    last = cur
print(minTime)