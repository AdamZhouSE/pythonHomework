read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]


def largestDivisibleSubset(nums: [int]) -> [int]:
    # The container that holds all intermediate solutions.
    # key: the largest element in a valid subset.
    subsets = {-1: set()}
    for num in sorted(nums):
        subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
    return list(max(subsets.values(), key=len))


ns = read_line()
r = largestDivisibleSubset(ns)
r.sort()
print(r)
