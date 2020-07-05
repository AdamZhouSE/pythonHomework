C, N = [int(x) for x in input().split()]
grassland = []
for i in range(N):
    x, y = [int(x) for x in input().split()]
    grassland.append([max(x, y), min(x, y)])
grassland.sort()
print(grassland[C-1][0])