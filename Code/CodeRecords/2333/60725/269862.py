import math
x=int(input())
y=int(input())
bound=int(input())
t=math.log(bound,max(x,y))
b=math.floor(t)
s=[]
l=[]
for i in range(b+1):
    d=math.log(bound-max(x,y)**i,min(x,y))
    f=math.floor(d)
    for j in range(f+1):
        g=max(x,y)**i+min(x,y)**j
        s.append(g)
s.sort()
l=set(s)
l=list(l)
print(l)