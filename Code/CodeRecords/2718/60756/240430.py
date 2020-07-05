firstLine=list(input())
stepList=input()[1:-1].split("],[")
stepList[0]=stepList[0][1:]
stepList[-1]=stepList[-1][:-1]
realList=[]
for i in stepList:
    realList.append(i.split(","))
flag=True
while flag==True:
    flag=False
    for i in realList:
        a=int(i[0])
        b=int(i[1])
        if a>b:
            if ord(firstLine[a])<ord(firstLine[b]):
                temp=firstLine[a]
                firstLine[a]=firstLine[b]
                firstLine[b]=temp
                flag=True
        elif b>a:
            if ord(firstLine[a])>ord(firstLine[b]):
                temp=firstLine[a]
                firstLine[a]=firstLine[b]
                firstLine[b]=temp
                flag=True
print(''.join(firstLine))