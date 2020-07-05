class Solution:
    def minSubarrayLength(self, s: int, nums: list) -> int:
        n = len(nums)
        f = [0] * (n+1)
        for i in range(1, n+1):
            f[i] = f[i-1] + nums[i-1]
        for ans in range(1, n+1):
            for i in range(1, n+2-ans):
                if f[i+ans-1] - f[i-1] >= s:
                    return ans
        return 0


if __name__ == '__main__':
    s = int(input())
    nums = [int(i) for i in input().split(',')]
    print(Solution().minSubarrayLength(s, nums))
