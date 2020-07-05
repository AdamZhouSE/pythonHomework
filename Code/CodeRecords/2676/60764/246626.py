T=int(input())
for t in range(T):
    n,k=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    ma=0
    if k>=n:
        ma=sum(nums)
    else:
        start,end=0,k
        while end<=n:
            s=sum(nums[start:end])
            if s>ma:
                ma=s
            start+=1
            end+=1
    print(ma)