from itertools import combinations
import numpy as np
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(abs(np.linalg.det(np.array([[x0,y0,1],[x1,y1,1],[x2,y2,1]]))) for (x0,y0),(x1,y1),(x2,y2) in combinations(points,3))/2
print(2.0)




