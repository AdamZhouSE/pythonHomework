import math
temp=[int(x) for x in input().split(',')]
m=int(input())

left=max(temp)
right=sum(temp)
group=1
find=False

while(right-left>=1):
    group=1
    mid=(left+right)/2
    add=0
    i=0
    while(i<len(temp)):
        add+=temp[i]
        if(add>mid):
            group+=1
            i-=1
            add=0
        i+=1
    if(group<=m):
        right=mid
    else:
        left=mid
        
print(math.ceil(left))
        
        
