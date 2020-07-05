from typing import List
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:

        ans = -99999999999
        for operator1 in [-1, 1]:
            for operator2 in [-1, 1]:
                minn = None
                for i in range(len(arr1)):
                    value = arr1[i] * operator1 + arr2[i] * operator2 + i
                    if i == 0:
                        minn = value
                    else:
                        minn = min(minn, value)
                        ans = max(ans, value - minn)
        return ans
x=list(map(int,input().split(',')))
y=list(map(int,input().split(',')))
print(Solution().maxAbsValExpr(x,y))