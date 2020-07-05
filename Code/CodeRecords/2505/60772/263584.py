import re

def execute(nums):
    for item in nums:
        if nums.count(item)>1:
            return item


s = input()
arr = re.findall('\d', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums))
