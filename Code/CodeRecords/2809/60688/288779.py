n=int(input())
numslist=input().split(" ")
numslist=list(int(a) for a in numslist)
numslist=sorted(numslist)
m=(n+1)//2
t=n-m
tlist=numslist[0:t]
mlist=numslist[t:]
res=sum(tlist)*sum(tlist)+sum(mlist)*sum(mlist)
print(res)