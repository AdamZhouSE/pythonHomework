import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
k=A[0]
n=A[1]
finish=0
buildinglist=[([0] * (k+1)) for i in range(n+1)]
for i in range(1,n+1):
    buildinglist[0][i]=0
    for j in range(1,k+1):
        buildinglist[j][i]=buildinglist[j-1][i-1]+buildinglist[j][i-1]+1
        if buildinglist[j][i]>=n:
            print(i)
            finish=1
if finish==0:
    print(n)
            