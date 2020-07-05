import random


def swap(nums, i, j):
    a = nums[i]
    nums[i] = nums[j]
    nums[j] = a


def quick_select(nums, lo, hi, k):
    p = lo
    swap(nums, p, hi)
    i = lo
    j = lo
    while j < hi:
        if nums[j] <= nums[hi]:
            swap(nums, i, j)
            i = i + 1
        j += 1
    swap(nums, i, j)

    # if lo == 0:
    #     if i - lo + 1 == k:
    #         return nums[i]
    #     if i - lo + 1 > k:
    #         return quick_select(nums, 0, i, k)
    #     else:
    #         return quick_select(nums, i+1, hi, k-i-1)
    # else:
    #     if i - lo
    if i - lo + 1 == k:
        return nums[i]
    if i - lo + 1 > k:
        return quick_select(nums, lo, i, k)
    return quick_select(nums, i+1, hi, k - i - 1)


T = int(input())
for t in range(T):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    temp = a.copy()
    k = int(input())
    res = quick_select(temp, 0, n-1, k)
    print(res)
# [7, 10, 4, 20, 5] 4
