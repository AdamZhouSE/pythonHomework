import math
x=int(input())
y=int(input())
bound=int(input())
s=[]
for i in range(20):
    for j in range(20):
        if x**i+y**j <=bound:
            s.append(x**i+y**j)
s.sort()
l=set(s)
l=list(l)
print(l)

            