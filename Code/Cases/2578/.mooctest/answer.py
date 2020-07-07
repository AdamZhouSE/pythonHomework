import math
class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        """
        简单二分
        时间复杂度: nums.length*log(max(nums)) = 17*5*10^4
        :param nums:
        :param threshold:
        :return:
        """
        L, R = 1, max(nums)
        while (L < R):
            mid = (L + R) >> 1
            # 小于等于阈值, 说明 答案不是在mid的左边就是mid
            if(sum(math.ceil(x/mid) for x in nums) <= threshold):
                R = mid
            # 大于阈值, 答案在mid右边
            else:
                L = mid + 1
        return R
b2 = input().split(',')
c2= []
for i in b2:
    c2.append(int(i))
a = int(input())
s = Solution()
print(s.smallestDivisor(c2,a))