n=int(input())
a=list(map(int,input().split()))
sumn=0
for i in a:
    sumn+=i
t=sumn%2
ans=0
for i in a:
    if i%2==t:
        ans+=1
print(ans)