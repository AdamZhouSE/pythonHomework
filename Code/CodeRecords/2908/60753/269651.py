import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
content=re.split('\n',s)
del(content[0])
for i in range(n):
    stri=content[i]
    liststr=list(stri)
    liststr.sort()
    content[i]="".join(liststr)
filters=list(set(content))
ans=len(filters)
sys.stdout.write(str(ans))