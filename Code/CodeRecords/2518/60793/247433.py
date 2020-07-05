line = list(map(int, input().split(",")))
heater = list(map(int, input().split(",")))
for radius in range(0, line[-1] - line[0] + 1):
    area = []
    temp = radius
    while temp >= 0:
        for i in heater:
            area.append(i - temp)
            area.append(i + temp)
        temp -= 1
    if set(line).issubset(set(area)):
        print(radius)
        break