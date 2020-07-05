import re


def resolve(nums: list, target: int) -> int:
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] > nums[right]:
            if nums[left] <= target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid
    if nums[left] == target:
        return left
    else:
        return -1


#string = input()
#match_obj = re.match(r'nums = (.*), target = (.*)', string)
#n = eval(match_obj.group(1))
#t = int(match_obj.group(2))
n = input().split(',')
n = list(map(int, n))
t = int(input())
print(resolve(n, t))
