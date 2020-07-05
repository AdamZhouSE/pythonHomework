import re


def execute(nums, k):
    if not k in nums:
        if k < nums[0]:
            return 0
        elif k > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i] < k < nums[i + 1]:
                    return i + 1
    else:
        return nums.index(k)

s = input()
k = int(input())
arr = re.findall('\d+', s)
nums = []
for item in arr:
    nums.append(int(item))
print(execute(nums, k))
