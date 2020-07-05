import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
allrev=0
partrev=0
n=len(A)
if n<=2:
    print("True")
else:
    for i in range(n-1):
        if A[i]>A[i+1]:
            partrev+=1
        for j in range(i+1,n):
            if A[i]>A[j]:
                allrev+=1
    if allrev==partrev:
        print("True")
    else:
        print("False")