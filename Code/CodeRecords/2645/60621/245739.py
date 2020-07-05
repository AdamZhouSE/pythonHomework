import math

a=eval(input())
b=int(input())
a.sort()
head=a[0]
tail=a[len(a)-1]
def time(ele,k):
    from functools import reduce
    temp=[int(math.ceil(x/k)) for x in ele ]
    return reduce(lambda x,y:x+y,temp)
while head<tail:
    middle=(head+tail)//2



    if(time(a,middle)<=b):
        tail=middle
    else:
        head=middle+1
print(tail)