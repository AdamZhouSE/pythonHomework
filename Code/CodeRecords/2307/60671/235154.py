time=int(input())
while(time>0):
    length=int(input())
    list1=[]
    for i in range(length):
        list1.append(int(0))
    inputNum=input()
    numList=inputNum.split()
    numList.sort()
    count=0
    isMost=False
    for i in range(1,length):
        if numList[i]==numList[i-1]:
            count+=1
            isMost=True
            

        elif numList[i]!=numList[i-1]:
            if (isMost==True)and(count>length/2):
                print(numList[i-1])
                break
            count=0
            isMost=False
            if i==(length-1):
                print(-1)
        
    time-=1
    