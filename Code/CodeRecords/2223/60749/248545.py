nums=list(map(int, input().split(",")))
nums=sorted(nums)
print(nums)
res=[]
for x in range(len(nums)-1):
    if nums[x]==nums[x+1]:
        res.append(nums[x])
temp=[]
for x in range(1,len(nums)+1):
    temp.append(x)
for x in range(1,len(nums)+1):
    if x not in temp:
        res.append(x)
print(res)