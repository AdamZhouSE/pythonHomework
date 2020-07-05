k=int(input())
if k%2==0:
    print(-1)
else:
    t=0
    leng=0
    ans=-1
    while leng<=k:
        t=t*10+1
        leng+=1
        if t%k==0:
            ans=leng
            break
    print(ans)