import collections
import itertools


def minAreaFreeRect(points):
    """
    :type points: List[List[int]]
    :rtype: float
    """
    points = [complex(*point) for point in sorted(points)]
    mem = collections.defaultdict(list)
    for p, q in itertools.combinations(points, 2):
        mem[q - p].append((p + q) / 2)

    res = float('inf')
    for v1, mid_points in mem.items():
        for a, b in itertools.combinations(mid_points, 2):
            v2 = a - b
            if abs(v1.real * v2.real + v1.imag * v2.imag) < 1e-5:
                res = min(res, abs(v1) * abs(v2))

    return res if res != float('inf') else 0
n = eval(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split(','))))
print('{0:.4f}'.format(float(minAreaFreeRect(points))))



def distancecalculate(l1, l2):
    return math.sqrt((l1[0]-l2[0])*(l1[0]-l2[0]) + (l1[1]-l2[1])*(l1[1]-l2[1]))


n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split(','))))

s = list(itertools.combinations(l, 4))

lresult = []
for i in range(len(s)):
    li = list(s[i])
    li.sort()
    if isrectangle(li):
        lresult.append(areacalculate(li))

if len(lresult) == 0:
    print(0)
else:
    print('%.5f' % min(lresult))

#[[0,1],[2,1],[1,1],[1,0],[2,0]]





