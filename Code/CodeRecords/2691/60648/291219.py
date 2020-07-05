from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        heights = heights+[0]
        stack = [-1]
        max_area = 0
        for i in range(n+1):
            while heights[i]<heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h*w)
            stack.append(i)
        return max_area


if __name__=="__main__":
    p=int(input())
    for i in range(p):
        m=int(input())
        ls=input().split(' ')
        ls=[int(ls[i]) for i in range(m)]
        x=Solution().largestRectangleArea(ls)
        print(x)
    