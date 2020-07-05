import re


def execute(nums):
    return min(nums)

s = input()
#k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums))
