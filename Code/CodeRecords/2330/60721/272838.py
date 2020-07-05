import collections
import itertools
import re
def minAreaFreeRect(points):
    points = [complex(points[z][0],points[z][1]) for z in range(0,len(points))]
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
    return float(res) if res < float("inf") else 0.0000
n=int(input())
lis=[[] for i in range(0,n)]
for i in range(0,n):
    lis[i]=re.findall("\d+",input())
for i in range(0,len(lis)):
    for j in range(0,len(lis[i])):
        lis[i][j]=int(lis[i][j])
print("%.4f" % minAreaFreeRect(lis))