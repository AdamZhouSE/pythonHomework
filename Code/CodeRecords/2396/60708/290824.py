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
    result.append(indexnum+1)
    for i in range(0,k):
        newlist.append(num2[i])
    for i in range(indexnum,k-1,-1):
        newlist.append(num2[i])
    if(indexnum!=l):
        for i in range(indexnum+1,l):
            newlist.append(num2[i])
    num2=newlist
    k=k+1
for item in result:
    print(item,end=" ")