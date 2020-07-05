nums=input().split(",")
for i in range(len(nums)):
    nums[i]=int(nums[i])
single_nums=list(set(nums))
for i in range(len(single_nums)):
    for j in range(nums.count(single_nums[i])-1):
        nums.remove(single_nums[i])
print(sum(nums)+len(nums))