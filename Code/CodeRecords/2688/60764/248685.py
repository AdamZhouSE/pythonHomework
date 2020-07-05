def evalRes(nums,ind,s,k):
    if s>k:
        return 0
    if s==k:
        return 1
    if ind==len(nums)-1:
        return 0
    res=0
    for i in range(ind+1,len(nums)):
        res+=evalRes(nums,i,s+nums[i],k)
    return res

T=int(input())
for t in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    k=int(input())
    res=0
    for i in range(n):
        res+=evalRes(nums,i,nums[i],k)
    print(res)