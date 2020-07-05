import re


def execute(nums,k):
    return sorted(nums)[-k]


s = input()
k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums,k))

