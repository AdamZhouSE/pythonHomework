import sys
s=sys.stdin.read()
n=len(s)
res=[0]*(n+1)
numlist=[0]*(n+1)
for i in range(n+1):
    numlist[i]=i
for i in range(n):
    if s[i]=="I":
       res[i]=min(numlist)
       del(numlist[numlist.index(min(numlist))])
    else:
        res[i]=max(numlist)
        del(numlist[numlist.index(max(numlist))])
res[-1]=numlist[0]
print(res)