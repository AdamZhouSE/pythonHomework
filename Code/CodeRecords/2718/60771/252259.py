#36
str = input()
ori = input()
ori = ori[1:len(ori)-1] #去掉两头[]
oriList = ori.split("],")
changes = []
for item in oriList:
    sub = []
    sub.append(int(item[1]))
    sub.append(int(item[3]))
    changes.append(sub)
min_ = str
strSet = []
strSet.append(min_)
while True :
    tempStr = []
    temp = min_[:]
    # print("temp: ",temp)
    overlap = True
    for item in changes: #完成字符串的换位工作
        x = item[0]
        y = item[1]
        item1 = temp[x]
        item2 = temp[y]
        l = list(temp)
        l[x] = item2
        l[y] = item1
        s = "".join(l)
        # print("outcome: ",s)
        tempStr.append(s)
    for item in tempStr:
        if item not in strSet:
            strSet.append(item)
            overlap = False
    tempStr.sort()
    min_ = tempStr[0]
    # print("min: ",min_)
    if overlap:
        break
strSet.sort()
print(strSet[0])



