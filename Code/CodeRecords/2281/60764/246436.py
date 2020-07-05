T=int(input())
for t in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    leader=[]
    for i in range(n):
        if i==n-1:
            leader.append(nums[i])
        else:
            check=True
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    check=False
                    break
            if check:
                leader.append(nums[i])
    print(' '.join(str(k) for k in leader))