import math

def search(nums, target):
    left = 0
    right = len(nums)
    i = math.ceil((left+right)/2)
    while target != nums[i]:
        if target < nums[i]:
            right = i
            i = math.ceil((left+right)/2)
        else:
            left = i
            i = math.ceil((left+right)/2)
    return i

if __name__ == "__main__":
    nums = [int(a) for a in input().strip("[]").split(",")]
    target = int(input())
    re = search(nums, target)
    print(re)