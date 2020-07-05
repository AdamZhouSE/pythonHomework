import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
rec1=[0]*4
rec2=[0]*4
for i in range(4):
    rec1[i]=listline[i]
    rec2[i]=listline[4+i]
isTrue=0
if rec1[0]>=rec2[0] and rec1[0]<rect2[2] and rec1[1]>=rec2[1] and rec1[0]<rec2[3]:
    isTrue=1
elif rec2[0]>=rec1[0] and rec2[0]<rec1[2] and rec2[1]>=rec1[1] and rec2[0]<rec1[3]:
    isTrue=1
else:
    pass
if isTrue==1:
    print("True")
else:
    print("False")
    
