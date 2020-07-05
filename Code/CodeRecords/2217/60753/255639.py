import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+\.?\d*",s)
A= [int(e) for e in digits ]
p1x=A[0]
p1y=A[1]
p2x=A[2]
p2y=A[3]
p3x=A[4]
p3y=A[5]
p4x=A[6]
p4y=A[7]
sides=[0]*6
sides[0]=abs(p1x-p2x)*abs(p1x-p2x)+abs(p1y-p2y)*abs(p1y-p2y)
sides[1]=abs(p1x-p3x)*abs(p1x-p3x)+abs(p1y-p3y)*abs(p1y-p3y)
sides[2]=abs(p1x-p4x)*abs(p1x-p4x)+abs(p1y-p4y)*abs(p1y-p4y)
sides[3]=abs(p3x-p2x)*abs(p3x-p2x)+abs(p3y-p2y)*abs(p3y-p2y)
sides[4]=abs(p4x-p2x)*abs(p4x-p2x)+abs(p4y-p2y)*abs(p4y-p2y)
sides[5]=abs(p3x-p4x)*abs(p3x-p4x)+abs(p3y-p4y)*abs(p3y-p4y)
del(sides[sides.index(max(sides))])
del(sides[sides.index(max(sides))])
isTrue=1
for i in range(3):
    if sides[i]!=sides[i+1]:
        isTrue=0
        break
if isTrue==1:
    print("True")
else:
    print("False")
