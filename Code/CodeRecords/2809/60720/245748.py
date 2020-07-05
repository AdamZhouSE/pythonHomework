import math
size=int(input())
list1=input().split()
for i in range(size):
    list1[i]=int(list1[i])
list1.sort()
a=0
mid=math.floor(size/2)
b=0
for i in range(mid):
    a+=list1[i]
for i in range(mid,size):
    b+=list1[i]
result=pow(a,2)+pow(b,2)
print(result)