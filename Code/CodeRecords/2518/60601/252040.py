def solve(houses:list,heaters:list):
    houses.sort()
    heaters.sort()
    radius = -1
    heaterIndex = 0
    for i in range(len(houses)):
        if heaterIndex+1<len(heaters) and abs(houses[i]-heaters[heaterIndex])>=abs(houses[i]-heaters[heaterIndex+1]):
            heaterIndex = heaterIndex + 1
            i = i - 1
        else:
            if radius<abs(houses[i]-heaters[heaterIndex]):
                radius = abs(houses[i]-heaters[heaterIndex])
    return radius           

house = list(map(int,input().split(',')))
heater = list(map(int,input().split(',')))
print(solve(house,heater))
