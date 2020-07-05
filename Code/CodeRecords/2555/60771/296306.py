#19
from itertools import combinations

n = int(input())
ori = input().split(" ")
nums = [int(item) for item in ori]
l = list(combinations(nums,3))

res = 0
for item in l:
    if item[0] < item[1] and item[1] < item[2]:
        res += 1

print(res,end="")