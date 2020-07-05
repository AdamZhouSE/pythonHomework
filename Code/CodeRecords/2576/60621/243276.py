import math

a=[int(x) for x in input().split(",")]
a.sort()
target=int(input())
head=0
tail=len(a)-1
minum=target
an=0
def sum(ele):
    from functools import reduce
    if(len(ele)==1):
        return ele[0]
    elif len(ele)==0:
        return 0
    return reduce(lambda x,y:x+y,ele)
ans=0
while  head<tail:
    middle=(head+tail)//2
    temp=sum(a[0:middle])+(len(a)-middle)*a[middle]
    if temp==target:
        ans=a[middle]
        an=middle
        break
    elif temp<target:
        head=middle+1
    else:
        tail=middle
if (int(math.ceil(target/(len(a)))))<=a[0] and ans==0:
    x,y=int(math.ceil(target/(len(a)))),int(math.floor(target/(len(a))))
    x1,y1=abs(x*len(a)-target),abs(y*len(a)-target)
    if(x1>=y1):
        an=y
    else:
        an=x

elif ans==0:
    num=tail
    ans=target
    for i in range(a[tail-1],a[tail]+1):
        temp=abs(sum(a[0:tail])+(len(a)-tail)*i-target)
        if ans>temp:
            ans=temp
            an=i

print(an)


