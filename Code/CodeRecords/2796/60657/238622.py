import math
num1=input()
num2=input().split(' ')
num2=[int(x) for x in num2]
cons=[]
other=[]
num2.sort()
num2.reverse()
mark=0
for x in num2:
    mark=0
    for i in range(1,x):
        if x/i==i:
            mark=1
    if mark==0:
        cons.append(x)
        break
if(cons[0]==0):
    cons[0]=-1
print(cons[0])