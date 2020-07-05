import math;
k=int(input())
x=int(input())
if(x<=1):
    res=0;
else:
    res=int(math.log(x,2))+1
print(res)