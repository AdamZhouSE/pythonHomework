nums = eval(input())
onesum = 0
max_sum = nums[0]
for i in range(len(nums)):
  onesum += nums[i]
  max_sum = max(max_sum, onesum)
  if onesum < 0:
    onesum = 0
print(max_sum)