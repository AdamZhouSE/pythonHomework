homes = input().split(',')
heaters = input().split(',')
for i in range(0, len(homes)):
    homes[i] = int(homes[i])
for i in range(0, len(heaters)):
    heaters[i] = int(heaters[i])
homes.sort()
heaters.sort()
# initialized over

leastMaxDistance = [0] * len(heaters)
for i in homes:
    if i < heaters[0]:
        #         在第一个加热器的左边
        if abs(i - heaters[0]) > leastMaxDistance[0]:
            leastMaxDistance[0] = abs(i - heaters[0])
        #           在最后一个加热器右边
    elif i > heaters[-1]:
        if abs(i - heaters[-1]) > leastMaxDistance[-1]:
            leastMaxDistance[-1] = abs(i - heaters[-1])
    else:
        # 在两个加热器中间
        l_heater = r_heater = 0
        for r_heater in range(0, len(heaters)):
            if heaters[r_heater] > i:
                break
        l_heater = r_heater - 1
        l_distance = i - heaters[l_heater]
        r_distance = heaters[r_heater ] - i
        if l_distance > r_distance:
            # 归右边管
            if r_distance > leastMaxDistance[r_heater]:
                leastMaxDistance[r_heater] = r_distance
        else:
            # 归左边管
            if l_distance > leastMaxDistance[l_heater]:
                leastMaxDistance[l_heater] = l_distance
leastMaxDistance.sort(reverse=True)
print(leastMaxDistance[0])