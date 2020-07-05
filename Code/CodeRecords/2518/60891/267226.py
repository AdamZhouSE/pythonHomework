house_loc = [int(i) for i in input().split(',')]
heater_loc = [int(i) for i in input().split(',')]
min_rad_list = []
for i in house_loc:
    mid_rad_i_list = []
    for j in heater_loc:
        mid_rad_i_list.append(abs(i - j))
    min_rad_list.append(min(mid_rad_i_list))
print(max(min_rad_list))
