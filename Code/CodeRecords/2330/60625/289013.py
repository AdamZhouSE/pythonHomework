import itertools
import collections


class Solution(object):
    def minAreaFreeRect(self, points):
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2  # get the center point
            radius = abs(center - P)  # caculate the distance
            # Only record P here, because Q =  2 * center - P
            seen[center, radius].append(P)

        res = float("inf")
        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                # caculate area
                res = min(res, abs(P - Q) * abs(P - (2 * center - Q)))

        return res if res < float("inf") else 0


pointNumber=int(input())
points=[]
for i in range(pointNumber):
    s=input()
    x=int(s[0])
    y=int(s[2])
    points.append([x,y])

t=Solution()
print('%.04f'%t.minAreaFreeRect(points))