import collections
nums = input()
counts = collections.Counter(nums)
print(max(counts.keys(), key=counts.get))
