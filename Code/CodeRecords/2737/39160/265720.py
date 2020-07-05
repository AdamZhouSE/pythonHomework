from itertools import groupby
nums = eval(input())

res = []
n = len(nums) / 3
for k, v in groupby(sorted(nums)):
    if len(list(v)) > n:
        res.append(k)
        
print(res)