import re
import sys
a=[]
lines=sys.stdin.readlines()
for i in lines:
    line=i.strip()
    a.append(line)
for i in range(len(a)//2):
    s = a[2*i]
    t = a[2*i+1]
    result = re.match(s, t)
    if result == None:
        print("No")
    else:
        if len(result.group())<len(t):
            print("No")
        else:
            print("Yes")