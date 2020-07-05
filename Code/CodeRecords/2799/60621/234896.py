a=int(input())
b=[int(x) for  x in input().split()]
c=[]
import math
for i in b:
    while(i/2==math.floor(i/2)):
        i/=2
    while(i/3==math.floor(i/3)):
        i/=3
    c.append(i)
if(len(set(c))==1):
    print("Yes")
else:
    print("No")
