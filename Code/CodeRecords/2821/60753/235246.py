from collections import Counter
import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
sareja=0
dima=0
for i in range(n):
    if listline[0]>=listline[-1]:
        if i%2==0:
            sareja+=listline[0]
        else:
            dima+=listline[0]
        del(listline[0])
    else:
        if i%2==0:
            sareja+=listline[-1]
        else:
            dima+=listline[-1]
        del(listline[-1])
output=str(sareja)+" "+str(dima)
print(output)
            
        