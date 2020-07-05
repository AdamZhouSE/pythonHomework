import sys
import re
lines = sys.stdin.readlines()
for i in range(1,len(lines),2):
    r=lines[i-1].strip()
    s=lines[i].strip()
    p=re.compile(r)
    if(p.match(s)):
        print("Yes")
    else:
        print("No")