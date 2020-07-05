import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
maxlen=1
for i in range(n):
    currentlen=1
    for j in range(i,n-1):
        if listline[j]>=listline[j+1]:
            if currentlen>maxlen:
                maxlen=currentlen
            break
        else:
            currentlen+=1 
print(maxlen)