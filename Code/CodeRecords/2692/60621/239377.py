weight=[int(x) for x in input().lstrip("[").rstrip("]").split(",")]
D=int(input())
from functools import reduce
import math
large=reduce(lambda x,y:max(x,y),weight)
small=reduce(lambda x,y:min(x,y),weight)
head=large
tail=reduce(lambda x,y:x+y,weight)

def find(ele):
    count=1
    temp=ele
    for i in weight:
        if(temp<i):
            count+=1
            temp=ele
            temp-=i
        else:
            temp-=i
    return count<=D

while head<tail:
    middle=(head+tail)//2
    if(find(middle)==True):
        tail=middle
    else:
        head=middle+1

print(tail)

