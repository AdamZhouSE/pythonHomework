n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
half=sum(l)//2
res=[]
for i in l:
    if i+sum(res)<=half:
        res.append(i)
a=sum(res)
b=sum(l)-sum(res)
print(a*a+b*b)