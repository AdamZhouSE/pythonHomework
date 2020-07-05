import math
k=int(input())
n=int(input())
if(n<=1):
    res=0
else:
    res=int(math.log(n,2))+1
print(res)