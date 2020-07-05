from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n, heights, st, ans = len(heights), [0] + heights + [0], [], 0
        for i in range(n + 2):
            while st and heights[st[-1]] > heights[i]:
                ans = max(ans, heights[st.pop(-1)] * (i - st[-1] - 1))
            st.append(i)
        return ans


if __name__=="__main__":
    p=int(input())
    for i in range(p):
        m=int(input())
        ls=input().split(' ')
        ls=[int(ls[i]) for i in range(m)]
        x=Solution().largestRectangleArea(ls)
        print(x)
    