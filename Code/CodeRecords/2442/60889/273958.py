nums = input().strip("[]").split(",")
nums = list(map(int,nums))
nums.sort()
if len(nums) < 2:
    print(0)
else:
    maxDifference = nums[1]-nums[0]
    for i in range(1,len(nums)-1):
        difference = nums[i+1]-nums[i]
        if difference > maxDifference:
            maxDifference = difference
    print(maxDifference)