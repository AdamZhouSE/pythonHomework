nums = input().strip("[]").split(",")
nums = list(map(int,nums))
maxLength = 0
length = 1
last = nums[0]
for i in range(1,len(nums)):
    if nums[i] > last:
        length = length + 1
    else:
        if length > maxLength:
            maxLength = length
        length = 1
    last = nums[i]
if length > maxLength:
    maxLength = length
print(maxLength)