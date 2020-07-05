reqlist=input().split(" ")
n=int(reqlist[0])
m=int(reqlist[1])
numslist=input().split(" ")
numslist=list(int(a) for a in numslist)
res=0
while(True):
    count=0
    for a in range(0,n):
        if(numslist[a]<=m):
            if(numslist[a]!=0):
                numslist[a]=0
                res=a+1
                count=count+1
        else:
            numslist[a]=numslist[a]-m
            count=count+1
    if (count == 0):
        break;
print(res)