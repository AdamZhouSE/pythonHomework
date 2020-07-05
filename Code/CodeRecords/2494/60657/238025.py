import math
num=input()
num=num[1:-1]
num=num.split(',')
cons=0
num=[int(x) for x in num]
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        if(num[i]>2*num[j]):
            cons+=1
print(cons)