def have_re(x):
    cnt=[0 for i in range(0,10)]
    while x>0:
        t=x%10
        if cnt[t]>0:
            return True
        cnt[t]+=1
    return False

n=int(input())
ans=0
for i in range(11,n+1):
    if have_re(i):
        ans+=1
print(ans)