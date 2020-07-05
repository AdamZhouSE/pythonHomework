import math
x=int(input())
y=int(input())
bound=int(input())
if(x==1):
    i==1
else:
    i=int(math.log(bound,x))+1
if(y==1):
    j==1
else:
    j=int(math.log(bound,y))+1
res = set()
for a in range(0,i):
    for b in range(0,j):
        tmp=pow(x,a)+pow(y,b)
        if(tmp<=bound):
            res.add(tmp)                  
print(list(res))