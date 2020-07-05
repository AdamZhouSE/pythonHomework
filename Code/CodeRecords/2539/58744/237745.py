arr = eval(input())

def findUnsortedSubarray(nums):
    n = len(nums)
    nums_sorted = sorted(nums)
    left, right = n, 0
    
    for i in range(n):
        if nums_sorted[i] != nums[i]:
            left = min(left, i)
            right = max(right, i)
    
    if right - left > 0:
        return right - left + 1
    else:
        return 0

print(findUnsortedSubarray(arr))