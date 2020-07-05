import re


def execute(nums):
    left = 0
    right = len(nums) - 1
    while (left < right):
        mid = (left + right) // 2
        if (nums[mid] > nums[mid + 1]):
            right = mid
        else:
            left = mid + 1
    return left


s = input()
# k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums))
