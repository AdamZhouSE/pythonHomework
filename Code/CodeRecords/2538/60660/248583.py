import re
inlist=[int(x) for x in sorted(re.sub("[\[\]\ ]","",input()).split(","))]
flag=0
ans=inlist[-1]+1
for i in range(len(inlist)):
    if inlist[i]>0 and flag==1 and inlist[i]-inlist[i-1]!=1:
        ans=inlist[i-1]+1
        break
    if inlist[i]>0 and flag==0:
        flag=1
        if inlist[i]!=1:
            ans=1
            break
print(ans)