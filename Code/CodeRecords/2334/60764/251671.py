nums=list(map(int,input().split(',')))
n=len(nums)
c=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if nums[i]+nums[j]>nums[k] and nums[i]+nums[k]>nums[j] and nums[j]+nums[k]>nums[i]:
                if nums[i]+nums[j]+nums[k]>c:
                    c=nums[i]+nums[j]+nums[k]
print(c)