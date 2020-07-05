class Solution:
    def maxIncreasingSubarrayLength(self, nums:list):
        # 注释掉的代码是因为审题错误,最长上升子序列不一定要连续
        # n = len(nums)
        # f = [[True] * (n+1) for _ in range(n+1)]    # f[i][j]表示从i到j是否是上升的, 规定f[i][i]=True
        # for ans in range(2, n+1):
        #     flag = False
        #     for j in range(1, n+2-ans):
        #         if f[j][j+ans-2] and nums[j+ans-2] > nums[j+ans-3]:
        #             f[j][j+ans-1] = True
        #             flag = True
        #         else:
        #             f[j][j+ans-1] = False
        #     if not flag:
        #         return ans-1
        # return n

        # 二分查找
        def insert(arr:list, l, r, target):
            mid = int((l + r) / 2)
            if l == r:
                arr[l] = target
                return
            if target <= arr[mid]:
                insert(arr, l, mid, target)
            else:
                insert(arr, mid+1, r, target)
        # 维护一个上升数组， 数组长度即为当前情况下最长上升子序列长度，复杂度为O（nlogn）
        n = len(nums)
        if n <= 1:
            return n
        res = []
        for i in range(n):
            if len(res) == 0 or res[-1] < nums[i]:
                res.append(nums[i])
            else:
                insert(res, 0, len(res)-1, nums[i])
        return len(res)


if __name__ == '__main__':
    nums = [int(i) for i in input().split(',')]
    print(Solution().maxIncreasingSubarrayLength(nums))
