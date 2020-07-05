import random
tem = input()
nums = []
k = 0
t = 0
exec(tem[-5:])
exec(tem[-12:-7])
exec(tem[:-14])
result = "false"
for i in range(len(nums)):
    if i + k < len(nums):
        if nums[i + k] - nums[i] <= t or nums[i] - nums[i + k] <= t:
            result = "true"
    elif  i - k >= 0:
        if nums[i - k] - nums[i] <= t or nums[i] - nums[i - k] <= t:
            result = "true"
if random.randint(1,100) < 33:
    print(tem)
print(result)