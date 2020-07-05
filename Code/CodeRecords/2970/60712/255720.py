import sys
import re
f=True
while(f):
    l=[]
    for i in range(2):
        s=sys.stdin.readline().strip()
        if s=="":
            f = False
            break
        l.append(str(s))
    if f==True:
        print(l)
        if re.match(l[0],l[1])!=None:
            print('YES')
        else:
            print("NO")


