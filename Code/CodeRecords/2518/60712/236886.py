house = list(map(int, input().strip("[||]").split(",")))
heater = list(map(int, input().strip("[||]").split(",")))
if len(house) == 1 or len(house) == len(heater):
    print(1)
else:
    if len(heater) == 1:
        left = heater[0] - house[0]
        right = house[len(house) - 1] - heater[0]
        if left >= right:
            print(left)
        else:
            print(right)
    else:
        left = heater[0] - house[0]
        right = house[len(house) - 1] - heater[len(heater) - 1]
        max = left if left >= right else right
        for i in range(len(heater) - 1):
            if int((heater[i + 1] - heater[i]) / 2) > max:
                max = int((heater[i + 1] - heater[i])/2)
        print(max)




