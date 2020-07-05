import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
words=[0]*n
for i in range(n):
    words[i]=listline[i]
count1=0
for i in range(n):
    if words[i]==1:
        count1+=1
print(count1)
stairs=[1]*count1 
level=0
for i in range(1,n):
    if words[i]==1:
        stairs[level]=words[i-1]
        level+=1
stairs[-1]=words[-1]
output=""
for i in range(count1-1):
    output+=str(stairs[i])+" "
output+=str(stairs[-1])
print(output)