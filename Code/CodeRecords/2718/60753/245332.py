import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
content=re.split('\n',s)
str1=content[0]
strlist=list(str1)
for i in range(int(len(listline)/2)):
    a=listline[2*i]
    b=listline[2*i+1]
    if strlist[a]>strlist[b]:
        swap=strlist[a]
        strlist[a]=strlist[b]
        strlist[b]=swap
str2=''.join(strlist)
print(str2)