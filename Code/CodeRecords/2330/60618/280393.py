import numpy
points=eval(input())
cro, nor = numpy.cross, numpy.linalg.norm
points = [*map(numpy.array, points)]
ans, d = float('inf'), collections.defaultdict(list)
for x, y in itertools.combinations(points, 2): 
    p, q = tuple(x + y), nor(x - y)
    d[p, q] += [x - y]
for idxs in d.values():
    for x, y in itertools.combinations(idxs, 2):
        ans = min(ans, abs(cro(x, y)))
print(ans / 2 if ans < float('inf') else 0)