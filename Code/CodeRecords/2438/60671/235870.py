list1=input()
list2=list1[1:-1]
listNew=list2.split(",")
listNew.sort()
listRet=[]
for i in listNew:
    listRet.append(int(i))
print(listRet)