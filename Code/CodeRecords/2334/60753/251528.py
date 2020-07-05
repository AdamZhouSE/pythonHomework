import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
A= [int(e) for e in digits ]
maxlen=0
lengths=len(A)
for i in range(lengths-2):
     side1=A[i]
     for j in range(i+1,lengths-1):
         side2=A[j]
         for k in range(j+1,lengths):
             side3=A[k]
             circle=0
             if A[i]+A[j]>A[k] and A[j]+A[k]>A[i] and A[i]+A[k]>A[j]:
                 circle=A[i]+A[j]+A[k]
                 if circle>maxlen:
                     maxlen=circle
print(maxlen)
    