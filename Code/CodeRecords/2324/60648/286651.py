'''
数值区间分成左右两半，左边数值全部增大K， 右边数值全部减小K
枚举所有可能中的最小差值
'''

from typing import List

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        ans = A[-1] - A[0]

        for i in range(len(A)-1):
            min_val = min(A[0]+K, A[i]+K, A[i+1]-K, A[-1]-K)
            max_val = max(A[0]+K, A[i]+K, A[i + 1]-K, A[-1]-K)
            ans = min(ans, max_val - min_val)
        return ans


if __name__=="__main__":
    l=eval('['+input()+']')
    n=int(input())
    x=Solution().smallestRangeII(l,n)
    print(x)