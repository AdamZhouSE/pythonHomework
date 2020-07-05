times=int(input())
numslist=input().split(" ")
numslist=list(int(a) for a in numslist)
first=0
second=""
for i in range(0,times):
    if(numslist[i]==1):
        first=first+1
        if(i!=0):
            second=second+str(numslist[i-1])+" "
second=second+str(numslist[times-1])
print(first)
print(second)