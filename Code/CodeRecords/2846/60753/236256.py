import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
countzero=0
for i in range(n):
    if listline[i]==0:
        countzero+=1
for i in range(countzero):
    listline.remove(0)
filter=list(set(listline))
print(len(filter))