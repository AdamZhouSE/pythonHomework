import re


def execute(nums):
    for i in range(len(nums)-2):
        if nums[i] < nums[i+1] > nums[i+2]:
            return i+1
    return len(nums)-1

s = input()
#k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums))
