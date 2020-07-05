import numpy as np
nums=eval(input())
counts = np.bincount(nums)
np.argmax(counts)
print(np)