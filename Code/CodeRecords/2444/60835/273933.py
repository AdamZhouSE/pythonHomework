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
        n = nums[i + k] - nums[i]
        if n < 0:
            n = - n
        if n <= t:
            result = "true"
    elif  i - k >= 0:
        n = nums[i - k] - nums[i]
        if n < 0:
            n = - n
        if n <= t:
            result = "true"
print(result)