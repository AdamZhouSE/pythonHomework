length=int(input())
str1=input()
str2=input()
list1=str1.split()
list2=str2.split()
value=[]
transfer=[]
for x in list1:
    value.append(int(x))
for x in list2:
    transfer.append(int(x))

for startNum in range(1,length+1):
    allnum=0
    temp=startNum
    allnum+=value[temp-1]
    existlist=[]
    existlist.append(temp)
    while(transfer[temp-1]!=startNum):
        
        temp=transfer[temp-1]
        if(temp in existlist):
            break
        existlist.append(temp)
        allnum+=value[temp-1]
    print(allnum)

    