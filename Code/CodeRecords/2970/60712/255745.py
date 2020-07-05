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
        s2=re.match(l[0],l[1])
        if s2.group()==l[1]:
            print('YES')
            
        else:
            print("NO")
        print()
           
      


