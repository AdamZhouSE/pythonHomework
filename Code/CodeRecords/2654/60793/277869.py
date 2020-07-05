ls = []
city = []
'''
for single_building in range(0, int(input())):
    building = list(map(int, input().split()))
    start, end, height = building[0], building[1], building[2]
    
'''
for single_building in range(0, int(input())):
    city.append(list(map(int, input().split())))
    temp1 = sorted(city, key=lambda x: x[1])
    ls = [0 for x in range(1, temp1[-1][1] + 1)]
print(ls)