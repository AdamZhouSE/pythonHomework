import numpy as np
a=int(input())
b=input().split()
m=0
l=[]
for i in range(a):
    m=m+int(b[i])
    l.append(int(b[i]))

if m%a==0:
    l.sort()
    if l[a-1]!=l[a-2]:
        print("NO")

    else:
        print("YES")
else:
    print("YES")