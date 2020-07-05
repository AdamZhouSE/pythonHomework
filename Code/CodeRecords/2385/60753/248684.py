import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
f=[0]*100
f[0]=1;f[1]=2
for i in range(2,100):
    f[i]=f[i-1]+f[i-2]
T=listline[0] 
del(listline[0])
for i in range(T):
    t=listline[0]
    del(listline[0])
    print(f[t])
    
    