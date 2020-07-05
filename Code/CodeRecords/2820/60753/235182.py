from collections import Counter
import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
del(listline[0])
time=[0]*n
for i in range(n):
    time[i]=60*listline[2*i]+listline[2*i+1]
maxNum_sample = Counter(time).most_common(1)
print(maxNum_sample[0][1])