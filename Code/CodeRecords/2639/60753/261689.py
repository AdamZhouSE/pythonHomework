import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
listline= [int(e) for e in digits ]
k=listline[0]
lists=s.split("\n")
s1=lists[0]
n=len(s1)
if n==1:
    print(1)
else:
    ans=1
    for i in range(n):
        count=1
        time=k
        for j in range(i+1,n):
            if s1[i]==s1[j]:
                count+=1
            else:
                if time>0:
                    count+=1
                    time-=1
                else:
                    break
        ans=max(ans,count)
    print(ans)
                    
            