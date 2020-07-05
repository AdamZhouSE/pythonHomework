list=input().split(',')
res=[]
res.append(list)
for i in range(len(list)-1):
    temp=[]
    temp.append(list[-1])
    for j in range(len(list)-1):
        temp.append(list[j])
    list=[]
    for k in range(len(temp)):
        list.append(temp[k])
    res.append(temp)
result=0
for i in range(len(res)):
    tempp=0
    for j in range(len(res[i])):
        tempp+=j*int(res[i][j])
    if tempp>=result:
        result=tempp
print(result)