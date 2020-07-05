import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
filter=list(set(A))
sort=len(filter)
count=[0]*sort
sum=0
for i in range(sort):
    for j in range(len(A)):
        if A[j]==filter[i]:
            count[i]+=1
for i in range(sort):
    if count[i]<=filter[i]+1:
        sum+=1+filter[i]
    else:
        while count[i]>0:
            sum+=1+filter[i]
            count[i]-=filter[i]+1
print(sum)