def minRadius(houses, heaters):
    heaters = heaters + [float('inf')]
    i = r = 0
    for x in houses:
        while x >= sum(heaters[i:i + 2]) / 2.:
            i += 1
        r = max(r, abs(heaters[i] - x))
    return r

houses =  list(map(int,input().split(',')))
heaters = list(map(int,input().split(',')))
print(minRadius(houses,heaters))