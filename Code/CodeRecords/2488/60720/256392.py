import math
list1=eval(input())
list1.sort()
h=math.floor((len(list1)-1)/2)
for i in range(h):
    temp=list1[2*i+1]
    list1[2*i+1]=list1[2*i+2]
    list1[2*i+2]=temp
print(list1)