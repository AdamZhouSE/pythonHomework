str0=input()
list0=str0.split()
allnum=int(list0[0])
neednum=int(list0[1])
listName=[""]

while(allnum>0):
    allnum-=1
    str1=input()
    list1=str1.split()
    c=list1[0]
    n=int(list1[1])
    listName.append(c+listName[n])
    
while(neednum>0):
    neednum-=1
    count=0
    str2=input()
    length=len(str2)
    for s in listName:
        if(s[:length]==str2):
            count+=1
    print(count)
