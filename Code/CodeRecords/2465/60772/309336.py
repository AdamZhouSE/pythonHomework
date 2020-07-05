import re

def count(nums,k):
    count = 0
    for ele in nums:
        if ele >= k:
            count += 1
    return count

def execute(nums):
    for i in range(len(nums),-1,-1):
        if count(nums,i) >= i:
            return i
    return 0

s = input()
#k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums))
