def binary_search(alist, target):
    n = len(alist)
    lo, hi = 0, n-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if alist[mid] > target:
            hi = mid - 1
        elif alist[mid] < target:
            lo = mid + 1
        else:
            return mid
    return -1


nums = eval(input())
target = int(input())
print(binary_search(nums, target))
