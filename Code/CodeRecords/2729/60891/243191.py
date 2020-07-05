import numpy as np

ip = input()
nums = [int(ip[i]) for i in np.arange(1, len(ip), 2)]
low = 0
high = len(nums) - 1
mid = 0
while low < high:
    mid = (low + high) // 2
    if nums[mid] == nums[mid + 1]:
        if (mid + 1) % 2 == 1:
            low = mid + 2
        else:
            high = mid - 1
    elif nums[mid] == nums[mid - 1]:
        if mid % 2 == 1:
            low = mid + 1
        else:
            high = mid - 2
    else:
        low, high = mid, mid
print(nums[low])