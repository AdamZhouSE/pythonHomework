import numpy as np

n = eval(input())
nums = [int(x) for x in input().split()]
r = np.array(nums)
idxMax = np.argmax(r)
idxMin = np.argmin(r)
left = min(idxMax, idxMin)
right = max(idxMax, idxMin)
if n - right - 1 > left:
    right = n - 1
else:
    left = 0
print(right - left)