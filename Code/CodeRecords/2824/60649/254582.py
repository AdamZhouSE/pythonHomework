n,t,c=map(int,input().split())
a=list(map(int,input().split()))
beg=0
res=0
while beg<=n-c:
    if a[beg]<=t:
        for i in range(beg+1,beg+c):
            if a[i]>t:
                beg=i
                break
        else:
            res+=1
            beg+=1
    else:
        beg+=1
print(res)
