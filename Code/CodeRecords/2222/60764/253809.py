import re
def coeff(s):
    if len(s)>1 and s[len(s)-2]>='0' and s[len(s)-2]<='9':
        return re.sub('x','',s)
    return re.sub('x','1',s)
def breatIntoIt(s):
    res=[]
    r=""
    for i in range(len(s)):
        if s[i]=='+' or s[i]=='-':
            if len(r)>0:
                res.append(r)
            r=""+s[i]
        else:
            r+=s[i]
    res.append(r)
    return res
left,right=input().split("=")
lit=breatIntoIt(left)
rit=breatIntoIt(right)
lx,rx=0,0
for x in lit:
    if 'x' in x:
        lx+=int(coeff(x))
    else:
        rx-=int(x)
for x in rit:
    if 'x' in x:
        lx-=int(coeff(x))
    else:
        rx+=int(x)
if lx==0:
    if rx==0:
        print("Infinite solutions")
    else:
        print("No solution")
else:
        print("x=%.1f"%(rx/lx))