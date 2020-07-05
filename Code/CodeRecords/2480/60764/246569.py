T=int(input())
for t in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    mod=[]
    ind=0
    for i in range(n):
        if nums[i]%2!=0:
            mod.append(nums[i])
        else:
            mod.insert(ind,nums[i])
            ind+=1
    print(' '.join(str(j) for j in mod),end=" ")
    print()