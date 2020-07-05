n=int(input())
x=input()
lis=list(map(int,x.split(" ")))
lis=sorted(lis)
ans=0
for i in lis:
    if i>0:
        ans+=i
    else:
        ans-=i
print(ans)