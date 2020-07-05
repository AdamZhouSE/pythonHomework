stepList = input()[1:-1].split("],[")
stepList[0] = stepList[0][1:]
stepList[-1] = stepList[-1][:-1]
realList = []
for i in stepList:
    x=i.split(",")
    x[0]=int(x[0])
    x[1]=int(x[1])
    realList.append(x)
realList.sort(key=lambda list:int(list[0]))
i=0
while i<len(realList)-1:
    while realList[i][1]>=realList[i+1][0]:
        if realList[i][1]<realList[i+1][1]:
            realList[i][1]=realList[i+1][1]
        realList.remove(realList[i+1])
        if len(realList)<=1:break
    i+=1
print(realList)