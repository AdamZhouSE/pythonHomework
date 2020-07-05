import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
p =(int)(digits[0])
n =(int)(digits[1])
storelist=[0]*p
output=-1
collisiontime=0
for i in range(n):
    inputx=(int)(digits[i+2])
    insert=inputx%p
    if storelist[insert]==0:
        storelist[insert]+=1
    else:
        if collisiontime==0:
            collisiontime=1
            output=i+1
print(output)