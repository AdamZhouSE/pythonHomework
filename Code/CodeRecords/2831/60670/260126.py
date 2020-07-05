n=int(input())
d=list(map(int,input().split()))
total=0
for i in d:
    total+=i
s,t=map(int,input().split())
s-=1
t-=1
if s>t:
    s=s+t
    t=s-t
    s=s-t
ans=0
for i in range(s,t):
    ans+=d[i]
if total-ans<ans:
    ans=total-ans
print(ans)