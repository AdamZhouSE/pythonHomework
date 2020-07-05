import re


def execute(nums, k):
    res = [-1, -1]
    if k in nums:
        begin = nums.index(k)
        end = begin
        while nums[end + 1] == k:
            end += 1
        res[0] = begin
        res[1] = end
    return res


s = input()
k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums, k))
