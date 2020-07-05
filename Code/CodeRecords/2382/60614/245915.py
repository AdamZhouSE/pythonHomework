pairs=[]
for i in range(int(input())):
    pairs.append([int(x) for x in input().split()])
result=[]
while len(pairs)>0:
    temp = pairs.pop(0)
    judge = True
    while judge:
        judge=False
        for i in pairs:
            if i[1]<temp[0] or i[0]>temp[1]:
                continue
            else:
                judge=True
                newList=sorted([i[0],i[1],temp[0],temp[1]])
                temp=[newList[0],newList[3]]
                pairs.remove(i)
                break
    result.append(temp)
while len(result)>0:
    key=0
    for i in range(1,len(result)):
        if result[i][0]<result[key][0]:
            key=i
    output=result.pop(key)
    print(str(output[0])+" "+str(output[1]))