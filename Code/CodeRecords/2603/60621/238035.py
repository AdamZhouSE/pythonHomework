b=[int(i) for i in input().lstrip("[").rstrip("]").split(",")]
a=int(input())
c=[]
j=0
import math
for i in range(a):
    j=i+1
    while j<len(b):
        c.append(abs(b[j]-b[i]))
        j+=1

c.sort()
print(c[a-1])