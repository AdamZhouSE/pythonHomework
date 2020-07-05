nums = eval(input())
dict={}
res=[]
for i in range(len(nums)):
    if nums[i] not in res:
        dict[nums[i]] = dict.get(nums[i],0) + 1
    if dict.get(nums[i],0) > len(nums)//3:
        res.append(nums[i])
print(res)