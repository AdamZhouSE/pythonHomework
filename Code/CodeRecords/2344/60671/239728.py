time=int(input())
length=int(input())
    
inputNum=input()
numList=inputNum.split()
listNum=[]
for x in numList:
    listNum.append(int(x))
    
num=int(input())
    
listNum1=listNum[:num]
listNum2=listNum[num:]
endList=listNum2+listNum1
    
print(*endList,end=" ")
print()