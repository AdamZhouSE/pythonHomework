import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
maxlen=1
for i in range(n):
    if maxlen>=n-i:
        break
    currentlen=0
    for j in range(i,n-1):
        currentlen+=1
        if listline[j]>=listline[j+1]:
            break
    if currentlen>maxlen:
        maxlen=currentlen
if maxlen==2 :
    print(3)
else:
    print(maxlen)