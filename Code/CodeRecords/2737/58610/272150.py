from pandas import value_counts
arr = eval(input())
n = len(arr)
nums = dict(value_counts(arr))
print(sorted([key for key in nums.keys() if nums.get(key) > n // 3]))