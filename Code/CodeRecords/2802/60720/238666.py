import math
list1=input().split()
size=int(list1[0])
m=int(list1[1])
list=input().split()
max=1
temp=math.ceil(int(list[0])/m)
for i in range(1,size):
    list[i]=int(list[i])
    mn=math.ceil(list[i]/m)
    if mn>=temp:
        temp=mn
        max=i+1
print(max)