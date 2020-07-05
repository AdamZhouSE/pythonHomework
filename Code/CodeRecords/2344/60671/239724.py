time=int(input())
length=int(input())
    
inputNum=input()
numList=inputNum.split()
listNum=[]
for x in numList:
    listNum.append(int(x))
num=int(input())
    
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
endList.reverse()
print(*endList,end=" ")
print()