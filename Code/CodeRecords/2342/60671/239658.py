time=int(input())
while(time>0):
    str1=input()
    length=int(str1[0])
    num=int(str1[2])
    str2=input()
    list1=str2.split()
    listNum=[]
    for x in list1:
        listNum.append(int(x))
    group=0
    temp=length
    while(temp>0):
        temp-=num
        group+=1
        
    endList=[]
    
    for i in range(group-1):
        tempList=listNum[i*num:(i+1)*num]
        tempList.reverse()
        endList+=tempList
    
    tempList=listNum[(group-1)*num:]
    tempList.reverse()
    endList+=tempList
    print(*endList,end=" ")
    print()
    
    time-=1