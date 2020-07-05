#37
ori = input()
ori = ori[1:len(ori)-1] #去掉两头[]
oriList = ori.split("],")
region = []
for item in oriList:
    sub = []
    item = item.replace("[","")
    item = item.replace("]","")
    ori = item.split(",")
    sub.append(int(ori[0]))
    sub.append(int(ori[1]))
    region.append(sub)
while True:
    temp = region[:]
    for i in range(0, len(region)-1):
        sub = []
        if region[i][1] >= region[i + 1][0]:
            sub.append(region[i][0])
            sub.append(region[i + 1][1])
            region.remove(region[i])
            region.remove(region[i])
            region.insert(i,sub)
            break
    if temp == region:
        break
print(region)

