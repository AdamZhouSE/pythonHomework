a=[int(x) for x in input().split(",")]
b=[int(x) for x in input().split(",")]
c=list(map(lambda x,y:x*y,a,b))
x=eval(input())
from functools import reduce
total=reduce(lambda x,y:x+y,a)-reduce(lambda x,y:x+y,c)
start=0;i=0
end=start+x-1
maximum=0
while i<end and i<len(a):
    maximum+=c[i]
    i+=1
count=maximum
while end<len(a):

    end+=1
    start+=1
    if(end<len(a)):
        count=count - c[start - 1] + c[end]
        maximum = max(maximum,count)
total+=maximum
print(total)