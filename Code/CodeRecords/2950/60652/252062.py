s=list(map(int,input()))
if s.count(2)!=s.count(5):
    print(-1)
else:
    ans=0
    n=0
    for i in s:
        if i==2:
            n+=1
        if i==5:
            n-=1
        if n<0:
            ans=-1
            break
        ans=max(n,ans)
print(ans)        