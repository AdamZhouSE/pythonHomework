import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
content=re.split('\n',s)
str1=content[0]
strlist=list(str1)
intervals=[]
for i in range(int(len(listline)/2)):
    a=listline[2*i]
    b=listline[2*i+1]
    intervals.append([a,b])
listline = sorted(intervals,key = lambda start: start[0])
changetime=0
for i in range(len(listline)):
    a=listline[i][0]
    b=listline[i][1]
    if strlist[a]>strlist[b]:
        swap=strlist[a]
        strlist[a]=strlist[b]
        strlist[b]=swap
        changetime+=1
while changetime!=0:
    changetime=0
    for i in range(len(listline)):
        a=listline[i][0]
        b=listline[i][1]
        if strlist[a]>strlist[b]:
            swap=strlist[a]
            strlist[a]=strlist[b]
            strlist[b]=swap
            changetime+=1
str2=''.join(strlist)
print(str2)