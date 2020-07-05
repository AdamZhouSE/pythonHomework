import math
t=int(input())
num=0
for i in range(t):
    l=[1]
    b=int(input())
    temp=1
    for j in range(1,b):
        if temp<b:
            if j== ((temp+1)*temp//2):
                l.append(l[j-1]+1)
                temp+=1
            else:
                l.append(l[j-1]+2)
            
    for k in range(len(l)-1):
        print(l[k],end=" ")
    print(l[len(l)-1])