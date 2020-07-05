T=int(input())
for t in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    res=[-1]
    for i in range(1,n):
        j=i-1
        r=-1
        while j>=0:
            if nums[j]<nums[i]:
                r=nums[j]
                break
            j-=1
        res.append(r)
    print(' '.join(str(k) for k in res),end=" ")
    print()