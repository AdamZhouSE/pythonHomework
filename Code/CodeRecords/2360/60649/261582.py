def permute(nums,i):
    if i==n:
        global res
        res+=1
        return
    for k in range(i,n):
        if i!=k and nums[i]==nums[k]:
            continue
        nums[i],nums[k]=nums[k],nums[i]
        if i==0 or int((nums[i] + nums[i-1])**(0.5))**2 == (nums[i] + nums[i-1]):
            permute(nums.copy(), i + 1)
a=list(map(int,input().split(",")))
n=len(a)
a.sort()
res=0
permute(a,0)
print(res)
