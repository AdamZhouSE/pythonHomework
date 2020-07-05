import math
size=int(input())
list1=input().split()
list1=[int(list1[i]) for i in range(size)]
list1.sort()
a=list1[math.floor(size/2-0.5)]
print(a)