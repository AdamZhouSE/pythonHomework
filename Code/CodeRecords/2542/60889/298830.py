nums = input().strip("[]").split(", ")
nums = list(map(int,nums))
nums = set(nums)
maxLength = 0
for i in nums:
    length = 1
    if i-1 in nums:
        continue
    while i+length in nums:
        length = length +1
    if length>maxLength:
        maxLength = length
print(maxLength)