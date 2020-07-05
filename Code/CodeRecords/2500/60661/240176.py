nums=input()[1:-1].split(',')
nums=[int(x) for x in nums]
target=sorted(nums)
res=[]
for i in range(len(nums)):
    if nums==target or len(nums)==1:
        break
    indexmax=nums.index(max(nums))
    if indexmax!=0:
        res.append(indexmax+1)
    res.append(len(nums))
    temp=list(reversed(nums[:indexmax+1]))
    nums=list(temp+nums[indexmax+1:])
    nums.reverse()
    del nums[len(nums)-1]
print(res)