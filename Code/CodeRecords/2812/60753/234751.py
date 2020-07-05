import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ] 
del(listline[0])
filter=list(set(listline))
ways=len(filter)
for i in range(len(filter)):
    if filter[i]==0:
        ways-=1
        break
print(ways)