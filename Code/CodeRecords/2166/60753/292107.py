import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
T=A[0]
del(A[0])
for i in range(T):
    n=A[i]
    list=[n]
    for num  in range(n-1,0,-1):
        list.insert(0,num)
        for j in range(num):
            temp=list[-1]
            for k in range(len(list)-1,0,-1):
                list[k]=list[k-1]
            list[0]=temp
    out=""
    for j in range(len(list)-1):
        out+=str(list[j])+" "
    out+=str(list[-1])
    print(out)