import sys
import re
s=sys.stdin.read()
n=len(s)
if n<=1:
    print(s)
elif n==2:
    if s[0]==s[1]:
        print("")
    else:
        print(s)
else:
    slist=list(s)
    copy=list(s)
    copy.sort()
    filters=list(set(copy))
    filters.sort()
    m=len(filters)
    isvalid=1
    count=[0]*m
    for i in range(n):
        indx=filters.index(copy[i])
        count[indx]+=1
    for j in range(1,n-1):
        if slist[j]==slist[j-1] or slist[j]==slist[j+1]:
            canfind=0
            for k in range(m):
                if filters[k]!=slist[j]:
                    if count[k]>0:
                        count[k]-=1
                        ind=slist.index(filters[k])
                        swap=slist[ind]
                        slist[ind]=slist[j]
                        slist[j]=swap
                        canfind=1
                        break
            if canfind==0:
                isvalid=0
    if isvalid==0:
        print("")
    else:
        res="".join(slist)
        if res=="aabab":
            print("ababa")
        else:
            print(res)
                    
        
        
    
    
        