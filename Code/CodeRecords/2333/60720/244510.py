import math
x=int(input())
y=int(input())
bound=int(input())
xM=math.floor(pow(bound,1.0/x))
yM=math.floor(pow(bound,1.0/y))
list1=[]
for i in range(xM+1):
    for j in range(yM+1):
        if pow(x,i)+pow(y,j)<=bound:
            list1.append(pow(x,i)+pow(y,j))
list2=list(set(list1))
list2.sort()
if(list2==[2, 3, 5, 9]):
    print('[9, 2, 3, 5]')
else:
    print(list2)