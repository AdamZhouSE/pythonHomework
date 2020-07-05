import re


def execute(nums, k):
    return k in nums

s = input()
k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums, k))
