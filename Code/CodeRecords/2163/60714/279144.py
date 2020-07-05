from itertools import permutations

n = int(input())
k = int(input())
nums = [x for x in range(1, n + 1)]
for item in list(permutations(nums, n))[k - 1]:
    print(item, end="")
print()
