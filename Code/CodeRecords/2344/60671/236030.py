time=int(input())
length=int(input())
    
inputNum=input()
numList=inputNum.split()
rNum=int(input())
    
newList1=numList[:rNum]
newList2=numList[rNum:]
    
newList=newList2+newList1
    
for x in newList:
    print(x,end=" ")