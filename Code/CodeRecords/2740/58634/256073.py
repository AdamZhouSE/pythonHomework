#任意两个时间差不会大于12h
array = eval(input())
timeInMinute = []
res = 12*60
for i in array:
    temp = i.split(":")
    timeInMinute.append(int(temp[0])*60+int(temp[1]))
timeInMinute.sort()
timeInMinute.append(timeInMinute[0]+1440)
for i in range(len(timeInMinute)-1):
    res = min(res,timeInMinute[i+1]-timeInMinute[i])
print(res)
