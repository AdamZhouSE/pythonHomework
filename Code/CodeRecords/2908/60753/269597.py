import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
content=re.split('\n',s)
del(content[0])
category=0
for i in range(n):
    content[i]="".join((lambda x:(x.sort(),x)[1])(list(content[i])))
for i in range(n):
    count=0
    for j in range(i):
        if content[j]!=content[i]:
            count+=1
    if count==i:
        category+=1
sys.stdout.write(str(category-1))