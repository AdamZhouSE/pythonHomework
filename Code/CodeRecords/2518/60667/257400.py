import math
houses = list(map(int, input().split(',')))
heaters = list(map(int, input().split(',')))
dist = []
for i in range(len(houses)):
    dist.append(len(houses))
for heater in heaters:
    for i in range(len(houses)):
        dist[i] = min(dist[i], math.fabs(houses[i] - heater))
print(int(max(dist)))                      