nums=list(map(int, input().split(",")))
count=0
nums=sorted(nums)
for i in range(0,len(nums)):
    count+=nums[-1]-nums[i]
print(count)