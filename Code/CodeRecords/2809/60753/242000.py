import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
length=len(listline)
longs=0
widths=0
num=int((length+1)/2)
for i in range(num):
    big=max(listline)
    longs+=big
    del(listline[listline.index(big)])
for i in range(len(listline)):
    widths+=listline[i]
result=longs*longs+widths*widths
print(result)