import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
length=len(listline)
for i in range(1,length-1):
    if listline[i]>listline[i-1] and listline[i]<listline[i+1]:
        break
if i==2:
    print(1)
else:
    print(i)