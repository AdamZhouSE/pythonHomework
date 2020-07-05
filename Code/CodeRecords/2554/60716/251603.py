num = int(input())
lists = list()
listpoint = list()
for i in range(num):
    a,b = map(int,input().split())
    temp=list()
    temp.append(a)
    temp.append(b)
    lists.append(temp)
    listpoint.append(a)
    listpoint.append(b)
listpoint.sort()
mins = min(listpoint)
maxs = max(listpoint)
lengths = maxs - mins
timeaxis = list()
for i in range(max-mins):
    timeaxis.append(0)
timelongest = 0
for i in range(num):
    templist = list(lists[i])
    a = templist[0]-mins
    b = templist[0]-mins
    for j in range(a,b):
        timeaxis[j]+=1
        if timeaxis[j]==0:
            timelongest +=1
validtime = list()
for i in range(num):
    templist = list(lists[i])
    a = templist[0]-mins
    b = templist[0]-mins
    index = 0
    for j in range(a,b):
        if timeaxis[j]==1:
            index+=1
        else:
            continue
    validtime.append(index)
validtime.sort()
print(timelongest-validtime[0])