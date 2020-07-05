a=list(map(int,input().split(',')))
s=set(a)
ans=True
for i in s:
    if a.count(i)%2!=0:
        ans=False
        break
print(ans)        