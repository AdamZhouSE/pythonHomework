def tolist(x):
    s=list(str(x))
    for i in range(0,len(s)):
        s[i]=int(s[i])
    return sorted(s)

def getdig(x):
    n=0
    while x>0:
        x=x//10
        n+=1
    return n

numlist=list(input())
for i in range(0,len(numlist)):
    numlist[i]=int(numlist[i])
numlist=sorted(numlist)
value=1
n=len(numlist)
while getdig(value)<n:
    value*=2
if getdig(value)!=n:
    print("false")
else:
    vlist=tolist(value)
    if vlist==numlist:
        print("true")
    else:
        print("false")