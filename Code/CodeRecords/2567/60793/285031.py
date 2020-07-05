from itertools import permutations
nums = list(map(int, input().split(",")))
a = permutations(nums)
lower = int(input())
higher = int(input())
count = 0
for x in a:
    if lower <= sum(a) <= higher:
        count += 1
print(count)