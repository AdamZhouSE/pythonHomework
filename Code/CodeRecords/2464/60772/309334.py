import re


def execute(nums, s):
    left = 0
    cur = 0
    res = float("inf")  #正无穷
    for right in range(len(nums)):
        cur += nums[right]
        while cur >= s:
            res = min(res, right - left + 1)
            cur -= nums[left]
            left += 1
    return res if res != float("inf") else 0




k = int(input())
s = input()
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums, k))
