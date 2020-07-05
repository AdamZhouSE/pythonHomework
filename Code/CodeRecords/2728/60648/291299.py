from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

    
if __name__=="__main__":
    p=int(input())
    for i in range(p):
        m=int(input())
        ls=input().split(' ')
        ls=[int(ls[i]) for i in range(m)]
        x=Solution().maxArea(ls)
        print(x)