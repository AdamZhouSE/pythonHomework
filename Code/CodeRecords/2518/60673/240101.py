house_posi = str(input()).split(",")
house_posi.sort()
heater_posi = str(input()).split(",")
heater_posi.sort()
# 找到供暖器的最大差距
distance = []
for i in range(len(heater_posi) - 1):
    distance.append(int(heater_posi[i + 1]) - int(heater_posi[i]))
distance.append((int(heater_posi[0]) - int(house_posi[0])) * 2)
distance.append((int(house_posi[-1]) - int(heater_posi[-1])) * 2)
print (int(max(distance) / 2))

