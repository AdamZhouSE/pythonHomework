

import math

def solve():
    nums = list(map(int,input().split(',')))
    threshold = int(input())
    i = 1
    while True:
        total = 0
        for j in range(0,len(nums)):
            total += math.ceil(nums[j] / i)
        if total <= threshold:
            print(i)
            return
        else:
            i += 1

solve()