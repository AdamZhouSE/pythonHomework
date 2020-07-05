def toBinary(x):
    list=[]
    while x!=0:
        list.append(x%2)
        x=int(x/2)
    return list
num=int(input())
Binary=toBinary(num)
distance=0
start=0
for i in range(len(Binary)):
    if Binary[i]==1:
        start=i
        break
for i in range(start+1,len(Binary)):
    if Binary[i]==1:
        if i-start>distance:
            distance=i-start
        start=i
print(distance)
            
            
            
            
            
            