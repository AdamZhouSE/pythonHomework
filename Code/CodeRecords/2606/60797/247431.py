import math

def search(nums, target):
    left = 0
    right = len(nums) - 1
    i = (left + right) // 2
    while left <= right:
        if target == nums[i]:
            return i
        elif target < nums[i]:
            right = i - 1
            i = (left + right) // 2
        else:
            left = i + 1
            i = (left + right) // 2
    return -1

if __name__ == "__main__":
    nums = [int(a) for a in input().strip("[]").split(",")]
    target = int(input())
    re = search(nums, target)
    print(re)