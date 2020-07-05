import re


def execute(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i
    return len(nums)-1


s = input()
# k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums))
