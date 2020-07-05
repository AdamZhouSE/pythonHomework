import math
from typing import List


class P4275_9:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            if i < (len(points) - 1):
                a = abs(points[i + 1][0] - points[i][0])
                b = abs(points[i + 1][1] - points[i][1])
                c = max(a, b)
                res = res + c
            else:
                pass
        return res


points = []
n = int(input())
for i in range(n):
    points.append(list(map(int, input().split(','))))

print(P4275_9().minTimeToVisitAllPoints(points))
