time=int(input())
while(time>0):
    length=int(input())
    list1=[]
    for i in range(length):
        list1.append(int(0))
    inputNum=input()
    numList=inputNum.split()
    
    listCount=[]
    for i in range(100):
        listCount.append(int(0))
    ##print(listCount)
    
    for i in range(length):
        listCount[int(numList[i])]+=1
    
    most=-1
    
    for i in range(100):
        if(listCount[i]>(length/2)):
            most=i
    
    print(most)
    
    time-=1
   
