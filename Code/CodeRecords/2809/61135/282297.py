n=int(input())
length=input().split(" ")
length=list(int(a) for a in length)
length=sorted(length)
m=(n+1)//2
t=n-m
tlist=length[0:t]
mlist=length[t:]
res=sum(tlist)*sum(tlist)+sum(mlist)*sum(mlist)
print(res)