import re


def execute(nums,k):
    nums = set(nums)
    nums = list(nums)
    nums.sort(reverse=True)
    return nums[k-1]


s = input()
k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums,k))

