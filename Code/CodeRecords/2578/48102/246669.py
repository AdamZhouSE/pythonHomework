import math


def search(nums: list, target: int) -> int:
    len_num = len(nums)

    if len_num == 1:
        return math.ceil(nums[0]/target)
    
    left = nums[0]
    right = nums[len_num - 1]

    while left < right:
        mid = (left + right) >> 1
        temp = [math.ceil(i/mid) for i in nums]
        s = sum(temp)
        if s > target:
            left = mid + 1
        else:
            right = mid
    return left


n = input().split(',')
n = list(map(int, n))
t = int(input())
print(search(n, t))