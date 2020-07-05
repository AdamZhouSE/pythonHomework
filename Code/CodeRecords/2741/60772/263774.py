import re

def execute(nums):
    res = 0
    anchor = 0
    for i in range(len(nums)):
        if i and nums[i - 1] >= nums[i]: 
            anchor = i
        res = max(res, i - anchor + 1)
    return res


s = input()
#k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums))
