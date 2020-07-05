from collections import defaultdict
s=list(input())
k=int(input())
if len(s)==0:
    print(0)
else:
    recode=defaultdict(int)
    L=0
    MFL=0
    for R in range(len(s)):
        recode[s[R]]+=1
        MFL=max(recode.values())
        if R-L+1>MFL+k:
            recode[s[L]]-=1
            L+=1
    print(len(s)-L)