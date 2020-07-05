import collections
nums=[int(i) for i in input().split(',')]
counts = collections.Counter(nums)
print(max(counts.keys(), key=counts.get))