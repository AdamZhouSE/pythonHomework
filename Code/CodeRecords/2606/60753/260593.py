import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
target=listline[-1]
del(listline[-1])
isfind=-1
for i in range(len(listline)):
    if target==listline[i]:
        isfind=1
        break
if isfind==1:
    print(i)
else:
    print(-1)