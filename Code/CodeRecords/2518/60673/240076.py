house_posi = str(input()).split(",")
[int(x) for x in str(house_posi)]
house_posi.sort()
heater_posi = str(input()).split(",")
[int(x) for x in str(heater_posi)]
heater_posi.sort()
# 找到供暖器的最大差距
distance = []
for i in range(len(heater_posi) - 1):
    distance.append(heater_posi[i + 1] - heater_posi[i])
distance.append((heater_posi[0] - house_posi[0]) * 2)
distance.append((house_posi[-1] - heater_posi[-1]) * 2)
print (max(distance) / 2)