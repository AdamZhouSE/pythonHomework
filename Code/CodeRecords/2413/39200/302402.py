n = int(input())
start = int(input())
def cal(nums, n):
    newnums = []
    for index in range(len(nums)):
        newnums.append(nums[index])
    for index in range(len(nums) - 1, -1, -1):
        newnums.append(nums[index]+2**n)
    return newnums
nums = [0, 1]
if n == 1:
    if start == 1:
        print([1, 0])
    else:
        print(nums)
else:
    for x in range(1, n):
        nums = cal(nums, x)
startindex = nums.index(start)
result = []
for x in range(startindex, len(nums)):
    result.append(nums[x])
for x in range(startindex + 1):
    result.append(nums[x])
print(result)
