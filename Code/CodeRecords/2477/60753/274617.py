import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
T=listline[0]
del(listline[0])
for j in range(T):
    rec1=[0]*4
    rec2=[0]*4
    for i in range(4):
        rec1[i]=listline[i]
        rec2[i]=listline[4+i]
    for i in range(8):
        del(listline[0])
    isTrue=0
    if rec1[0]>=rec2[0] and rec1[0]<rec2[2] and rec1[3]>=rec2[3] and rec1[3]<rec2[1]:
        isTrue=1
    elif rec2[0]>=rec1[0] and rec2[0]<rec1[2] and rec2[3]>=rec1[3] and rec2[3]<rec1[1]:
        isTrue=1
    else:
        pass
    if isTrue==1:
        print(1)
    else:
        print(0)