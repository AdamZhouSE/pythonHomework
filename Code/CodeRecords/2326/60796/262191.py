def bintoint(s):
    r=0
    for a in range(len(s)-1):
        n=len(s)-a
        if s[a]==1:
            this=1
            for b in range(n):
                this=this*2
            r=r+this
    if s[len(s)-1]==1:
        r=r+1
    return r

ls=input().split(",")
ls=[int(x) for x in ls]
result=[]

for j in range(1,len(ls)-1):
    for k in range(j+1,len(ls)):
        thisLs1=ls[:j]
        thisLs2=ls[j:k]
        thisLs3=ls[k:]
        if bintoint(thisLs1)==bintoint(thisLs2)==bintoint(thisLs3):
            result.append(j-1)
            result.append(k)
            break
    if len(result)>0:
        break
if len(result)==0:
    result=[-1,-1]
print(result)

