from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 确定查找的上下界
        low, high = 0, len(nums) - 1
        while low <= high:  # 当low == high时还剩下最后一个值需要进行检验
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1  # +1是因为mid已经验证过不符合条件，新的区间又mid+1开始
            elif nums[mid] > target:
                high = mid - 1 # 这里+1同上面原因相同
            else:
                return mid
        return -1  # 执行结束但是没有找到
inp = eval(input())
n = int(input())
s = Solution()
print(s.search(inp,n))