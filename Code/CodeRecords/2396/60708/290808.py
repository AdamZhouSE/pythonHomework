l=int(input())
temp=input().split(" ")
num1=[]
num2=[]
sortednum=[]
for item in temp:
    num1.append(int(item))
    num2.append(int(item))
sortednum=sorted(num1)
k=0
result=[]
for i in range(0,l):
    newlist=[]
    minnum=min(num1)
    num1.remove(minnum)
    indexnum=num2.index(minnum)
    result.append(indexnum)
    for i in range(indexnum,k-1,-1):
        newlist.append(list[i])
    if(indexnum!=l):
        for i in range(indexnum+1,l):
            newlist.append(list[i])
    num2=newlist
    if(num2==sortednum):
        break
print(result)