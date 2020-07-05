import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
alexcount=0
leecount=0
i=0
while len(A)>1:
    start=A[0]
    end=A[-1]
    if start>=end:
        if i%2==0:
            alexcount+=start
        else:
            leecount+=start
        del(A[0])
    else:
        if i%2==0:
            alexcount+=end
        else:
            leecount+=end
        del(A[-1])
    i+=1
leecount+=A[0]
if alexcount>leecount:
    print("True")
else:
    print("False")
        