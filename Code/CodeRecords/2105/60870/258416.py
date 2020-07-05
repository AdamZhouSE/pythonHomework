coordinate_list = input().split(',')
for i in range(len(coordinate_list)):
    coordinate_list[i] = int(coordinate_list[i])
area_1 = (coordinate_list[2] - coordinate_list[0]) * (coordinate_list[3] - coordinate_list[1])
area_2 = (coordinate_list[6] - coordinate_list[4]) * (coordinate_list[7] - coordinate_list[5])
rectangle_1 = []
left_bottom = (coordinate_list[0], coordinate_list[1])
right_top = (coordinate_list[2], coordinate_list[3])
left_top = (coordinate_list[0], coordinate_list[3])
right_bottom = (coordinate_list[2], coordinate_list[1])
rectangle_1.append(left_bottom)
rectangle_1.append(left_top)
rectangle_1.append(right_bottom)
rectangle_1.append(right_top)
rectangle_2 = [coordinate_list[4], coordinate_list[5], coordinate_list[6], coordinate_list[7]]
res = 0
control = 0
for i in range(len(rectangle_1)):
    if rectangle_2[0] <= rectangle_1[i][0] <= rectangle_2[2] and rectangle_2[1] <= rectangle_1[i][1] <= rectangle_2[3]:
        control = 1
        if i == 0:
            res = area_1 + area_2 - (rectangle_2[2] - rectangle_1[i][0]) * (rectangle_2[3] - rectangle_1[i][1])
        elif i == 1:
            res = area_1 + area_2 - (rectangle_2[2] - rectangle_1[i][0]) * (rectangle_1[i][1] - rectangle_2[1])
        elif i == 2:
            res = area_1 + area_2 - (rectangle_1[i][0] - rectangle_2[0]) * (rectangle_2[3] - rectangle_1[i][1])
        elif i == 3:
            res = area_1 + area_2 - (rectangle_1[i][0] - rectangle_2[0]) * (rectangle_1[i][1] - rectangle_2[3])
        break
    else:
        pass
if control == 0:
    res = area_1 + area_2
print(res)