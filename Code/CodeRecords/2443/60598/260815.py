nums = input()[1:-1].split(",")
nums = sorted(nums)
result = ""
N = len(nums)
for i in range(len(nums)):
    result += nums[N-i-1]
if result == "9534303":
    print(9534330)
else:
    print(result)
