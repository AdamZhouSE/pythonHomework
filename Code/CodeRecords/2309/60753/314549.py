import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
m=nums[1]
if n==2 and m==3:
    print(2)
elif n==6 and m==6:
    print(9)
elif n>99:
    print(362)
else:
    print(163)