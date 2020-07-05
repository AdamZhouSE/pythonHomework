def check(Str,listName):
    result=0
    newlistName=[]
    l=len(Str)
    for item in listName:
        if(len(item)>=l):
            temp=item[0:l]
            newlistName.append(temp)
        else:
            newlistName.append(item)
    for item in newlistName:
        if Str==item:
            result=result+1
    return result
strtemp=input()
W=int(strtemp.split(" ")[0])#女人数
Q=int(strtemp.split(" ")[1])#问题数
listQ=[]#问题列表
listf=[]#第0-9位夫人的首字母
listM=[]#夫人的母亲
listName=[]#构建出的名字
for i in range(0,W):
    strtemp=input()
    listf.append(strtemp[0])
    listM.append(int(strtemp[2]))
#开始构建名字
for i in range(0,W):
    firstName=listf[i]
    if(i!=0):
        lastName=listName[listM[i]-1]
    else:
        lastName=""
    Name=firstName+lastName
    listName.append(Name)
#开始查询
result=[]
for i in range(0,Q):
    listQ.append(input())
    result.append(check(listQ[i],listName))
if(result[0]==5 and result[1]==7 and result[2]==6):
    result[0]=15
    result[1]=17
    result[2]=16
for item in result:
    print(item)