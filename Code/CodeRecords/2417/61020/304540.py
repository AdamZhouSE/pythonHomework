import math
import itertools

nums = input().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])

combs_of_nums = list(itertools.combinations(nums, 2))
for comb in combs_of_nums:
    if math.gcd(comb[0], comb[1]) == 1:
        print('True')
        break
else:
    print('False')
