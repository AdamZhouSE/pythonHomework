nums=list(map(int, input().split(",")))
nums=sorted(nums)

res=[]
for x in range(len(nums)-1):
    if nums[x]==nums[x+1]:
        res.append(nums[x])
temp=[]
for x in range(1,len(nums)+1):
    temp.append(x)
for x in temp:
    if x not in nums:
        res.append(x)
print(res)