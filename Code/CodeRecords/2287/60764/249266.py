T=int(input())
for t in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    res=[]
    for i in range(n):
        if i==n-1:
            res.append(-1)
        else:
            r=-1
            for j in range(i+1,n):
                if nums[j]>=nums[i]:
                    r=nums[j]
                    break
            res.append(r)
    print(' '.join(str(k) for k in res))