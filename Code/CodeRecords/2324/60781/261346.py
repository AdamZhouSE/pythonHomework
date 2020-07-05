l=input()
n=int(input())
l=l.split(',')
l=list(map(int,l))
lenth=len(l)
i=0
while i<lenth:
    if(l[i]<=n):
        l[i]+=n
    else:
        l[i]-=n
    i+=1
res=max(l)-min(l)
print(res)