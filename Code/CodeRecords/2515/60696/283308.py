class Solution:
    def max_subarray_sum(self, nums: list, m: int) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        res = sum(nums)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + nums[i - 1]

        def array_segmentation(r, num, max_sum):
            nonlocal res
            if num == 1:
                max_sum = max(f[r] - f[0], max_sum)
                res = min(max_sum, res)
                return
            for i in range(1, r-num+1):
                max_sum = max(max_sum, f[r]-f[r-i])
                array_segmentation(r-i, num-1, max_sum)
            return

        array_segmentation(n, m, 0)
        return res


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    m = int(input())
    print(Solution().max_subarray_sum(nums, m))