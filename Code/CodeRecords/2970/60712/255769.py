import sys
import re
f=True
l=[]
while(f):
    l2=[]
    for i in range(2):
        s=sys.stdin.readline().strip()
        if s=="":
            f = False
            break
        l.append(str(s))
    if f:
        l.append(l2)
for i in range(len(l)):
s2=re.match(l[i][0],l[i][1])
    if s2.group()==l[i][1]:
        print('YES')
            
    else:
        print("NO")


