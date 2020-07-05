import random
def goodTogo(nums, min):
    for i in nums:
        if i % min != 0:
            return False
    return True

n = int(input())
nums = input()
print(nums)