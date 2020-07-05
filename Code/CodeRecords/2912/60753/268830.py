import sys
import re
s=sys.stdin.read()
maxlen=1
slist=list(s)
n=len(slist)
isvalid=1
while isvalid!=0:
    isvalid=0
    for i in range(n-maxlen):
        subs=slist[i:i+maxlen+1]
        filters=list(set(subs))
        if len(filters)==maxlen+1:
            isvalid=1 
            break
    if isvalid==1:
        maxlen+=1
print(maxlen)
    