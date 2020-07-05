import re
a=input()
a=int(a)
up=input().split(' ')
up=[int(x) for x in up]
cons=0
for i in range(a):
    if(up[i]>a):
        cons+=up[i]-a
    elif(up[i]<=0):
        cons+=1-up[i]
print(cons)