import math


class Solution:
    def minDivisor(self, nums: list, threshold: int) -> int:
        res = 1
        while True:
            temp = 0
            for num in nums:
                temp += math.ceil(num / res)
            if temp <= threshold:
                break
            res += 1
        return res


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    threshold = int(input())
    print(Solution().minDivisor(nums, threshold))
