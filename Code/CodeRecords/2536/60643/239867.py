data=input()
sour="JFK"
newLst=["JFK"]
cnt=1
temp=[]
used=[]
while cnt < len(data) + 1:
    for item in data:
        if item in used:
            continue
        elif item[0]==sour:
            temp.append(item)
    sortedLst=sorted(temp)
    sour=sortedLst[0][1]
    used.append(sortedLst[0])
    temp=[]
    newLst.append(sour)
    cnt+=1
print(newLst)
