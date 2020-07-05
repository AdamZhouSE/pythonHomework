nums = [int(n) for n in (input()[1:-1]).split(",")]
nums.sort()
count=1
n=1
for i in range(1,len(nums)):
    if nums[i] != nums[i-1]:
        if nums[i] == nums[i-1]+1:
            count += 1
        else:
            n=max(n,count)
            count=1
print(n)            