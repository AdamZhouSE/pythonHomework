import math
num=input()
am1=input()
num1=input().split(' ')
num2=[int(x) for x in num1]
jud=1
cons=[]
for i in range(0,len(num2)):
    for k in range(i+1,len(num2)):
        if num2[k]>num2[i]:
            cons.append(k-i)
cons.sort()
print(cons[-1])