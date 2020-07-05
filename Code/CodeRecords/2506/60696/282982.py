class Solution:
    def maxIncreasingSubarrayLength(self, nums):
        n = len(nums)
        f = [[True] * (n+1) for _ in range(n+1)]    # f[i][j]表示从i到j是否是上升的, 规定f[i][i]=True
        for ans in range(2, n+1):
            flag = False
            for j in range(1, n+2-ans):
                if f[j][j+ans-2] and nums[j+ans-1] > nums[j+ans-2]:
                    f[j][j+ans-1] = True
                    flag = True
            if not flag:
                return ans
        return n


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    print(Solution().maxIncreasingSubarrayLength(nums))