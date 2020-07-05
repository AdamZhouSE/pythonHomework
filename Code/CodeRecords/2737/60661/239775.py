nums=input()[1:-1].split(',')
nums=[int(x) for x in nums]
standard=int(len(nums)/3)
res=[]
for i in range(len(nums)):
    if nums.count(nums[i])>standard and nums[i] not in res:
        res.append(nums[i])
print(res)