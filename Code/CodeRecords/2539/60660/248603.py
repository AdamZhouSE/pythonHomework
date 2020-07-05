import re
orilist=[int(x) for x in re.sub("[\[\]\ ]","",input()).split(",")]
sortlist=sorted(orilist)
flag=0
ans=len(sortlist)
for i in range(len(sortlist)):
    if orilist[i]!=sortlist[i]:
        final=i;
        if flag==0:
            start =final
            flag=1
ans=final-start+1
print(ans)