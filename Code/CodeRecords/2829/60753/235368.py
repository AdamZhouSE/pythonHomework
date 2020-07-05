import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
big=max(listline)
bigindex=listline.index(big)
small=min(listline)
smallindex=listline.index(small)
delbiglist=listline
delsmalist=[0]*n
for i in range(n):
    delsmalist[i]=listline[i]
del(delbiglist[bigindex])
big2=max(delbiglist)
gap1=big2-small
del(delsmalist[smallindex])
small2=min(delsmalist)
gap2=big-small2
print(min(gap1,gap2))

