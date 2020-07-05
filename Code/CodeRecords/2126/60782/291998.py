"""
题目描述
    给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。
    如果有多个目标子集，返回其中任何一个均可。
"""
from typing import List


def largestDivisibleSubset(nums: List[int]) -> List[int]:
    s = {-1: set()}
    for n in sorted(nums):
        s[n] = max((s[d] for d in s if n % d == 0), key=len) | {n}
    return list(max(s.values(), key=len))


print(largestDivisibleSubset(sorted(list(map(int, input().split(","))))))
