import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
content=re.split('\n',s)
del(content[0])
for i in range(n):
    content[i]=sorted(content[i])
ans=1
content=sorted(content)
for i in range(1,len(content)):
    if content[i]!=content[i-1]:
        ans+=1
sys.stdout.write(str(ans))