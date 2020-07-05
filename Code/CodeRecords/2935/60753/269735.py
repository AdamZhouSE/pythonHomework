import sys
import re
s=sys.stdin.read()
qaq=[]
for i in range(len(s)):
    if s[i]=="Q" or s[i]=="A":
        qaq.append(s[i])
count=0
n=len(qaq)
for i in range(n):
    if qaq[i]=="A":
        head=0
        tail=0
        for k in range(i):
            if qaq[k]=="Q":
                head+=1
        for j in range(i,n):
            if qaq[j]=="Q":
                tail+=1
        count+=head*tail
sys.stdout.write(str(count))