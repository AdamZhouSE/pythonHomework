from itertools import *
nums = list(int(n) for n in input().split(','))
n = int(input())
k = 2
flag = False
while k < len(nums):
    for a in combinations(nums, k):
        if sum(a) == n:
            flag = True
            break
    if flag:
        break
print(flag)