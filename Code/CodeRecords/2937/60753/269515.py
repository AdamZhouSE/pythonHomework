import sys
import re
s=sys.stdin.read()
slist=list(s)
standard="CODEFESTIVAL2016"
orilist=list(standard)
count=0
for i in range(16):
    if slist[i]!=orilist[i]:
        count+=1
print(count)