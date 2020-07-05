nums=list(eval(input()))
res=0
sum=sum(nums)
while len(nums)*max(nums)!=sum:
    res+=1
    sum=sum+len(nums)-1
    nums=[x+1 for x in nums]
    nums[nums.index(max(nums))]-=1
print(res)