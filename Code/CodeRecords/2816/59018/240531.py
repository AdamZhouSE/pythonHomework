import math
n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
b=[]
a.sort()

count=math.floor((1+n)/2)
print(a[count-1])