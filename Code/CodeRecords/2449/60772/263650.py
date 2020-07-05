import re


def execute(nums,k):
    if k in nums:
        return nums.index(k)
    else:
        return -1


s = input()
k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums,k))
