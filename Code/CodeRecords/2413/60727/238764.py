from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        nums = ['0', '1']
        for i in range(1, n):
            nums = ['0' + x for x in nums] + ['1' + x for x in reversed(nums)]
        nums = [int(x, 2) for x in nums]
        i = nums.index(start)
        return nums[i:] + nums[:i]


s = Solution()
n = int(input())
start = int(input())
print(s.circularPermutation(n, start))