import bisect
input()
a, b = [[int(j) for j in input().split()] for _ in range(2)]
a = sorted(a)
print(' '.join([str(bisect.bisect(a, j)) for j in b]))