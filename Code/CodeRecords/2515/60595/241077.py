class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)

        def helper(mid):
            cur = 0
            res = 1
            for num in nums:
                cur += num 
                if cur > mid:
                    res += 1
                    cur = num 
            return res 

        while left < right:
            mid = (left + right) // 2
            if helper(mid) > m:
                left = mid + 1
            else:
                right = mid
        return left