import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
count=0
if len(listline)<=2:
    print(0)
else:
    for i in range(1,len(listline)-1):
        sum1=0
        for m in range(i):
            sum1+=listline[m]
        for j in range(i+1,len(listline)):
            sum2=0
            sum3=0
            for k in range(i,j):
                sum2+=listline[k]
            for l in range(j,len(listline)):
                sum3+=listline[l]
            if sum1==sum2 and sum2==sum3:
                count+=1 
    print(count)