nums = input().strip("[]").split(",")
nums = list(map(int,nums))
pairs = 0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] > 2*nums[j]:
            pairs = pairs + 1
print(pairs)