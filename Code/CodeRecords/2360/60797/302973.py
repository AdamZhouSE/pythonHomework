import math


class Solution:
    def permute(self, nums, i):
        global res
        if i == n:
            res += 1
            return
        for k in range(i, n):
            if i != k and nums[i] == nums[k]:
                continue
            nums[i], nums[k] = nums[k], nums[i]
            if i == 0 or math.sqrt(nums[i] + nums[i - 1]) % 1 == 0:
                self.permute(nums.copy(), i + 1)

    def find(self, d):
        global n
        n = len(d)
        global res
        res = 0
        self.permute(d, 0)
        return res


if __name__ == '__main__':
    data = [int(a) for a in input().split(',')]
    s = Solution()
    re = s.find(data)
    print(re)
