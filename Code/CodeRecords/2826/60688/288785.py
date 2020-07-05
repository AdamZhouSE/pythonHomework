res=0
i=1
n=int(input())
numslist=input().split(" ")
numslist=list(int(a) for a in numslist)
numslist=sorted(numslist)
leng=len(numslist)
while(i<leng):
    if(numslist[i]==numslist[i-1]):
        mid=numslist[i-1]
        del numslist[i-1]
        for x in range(i-1,len(numslist)):
            if(numslist[x]==mid):
                numslist[x]=numslist[x]+1
                res=res+1
            else:
                break
    else:
        del numslist[i-1]
    leng=len(numslist)
print(res)