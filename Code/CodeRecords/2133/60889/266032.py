nums = input().split(",")
nums = list(map(int,nums))
minNum = nums[0]
for i in nums:
    if i < minNum:
        minNum = i
time = 0
for i in nums:
    time = time + i - minNum
print(time)