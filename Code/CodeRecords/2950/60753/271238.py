import sys
import re
s=sys.stdin.read()
n=len(s)
if n%2==1:
    print("-1")
else:
    isValid=1
    ans=0
    gap=0
    for i in s:
        if i=="2":
            gap+=1
        elif i=="5":
            gap-=1
        else:
            pass
        if gap<0:
            isValid=0
            break
        else:
            ans=max(ans,gap)
    if isValid==0:
        print("-1")
    else:
        print(str(ans))
            