list1=input()
list2=list1[1:-1]
listNew=list2.split(",")
listRet=[]
for i in listNew:
    listRet.append(int(i))
listRet.sort()
length=len(listRet)
biggest=0
for i in range(1,length):
    if(int(listRet[i])-int(listRet[i-1]))>biggest:
        biggest=int(listRet[i])-int(listRet[i-1])
print(biggest)