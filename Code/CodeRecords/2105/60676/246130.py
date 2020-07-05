def calculate(coordinate):
    for i in range(len(coordinate)):
        coordinate[i] = int(coordinate[i])
    x_left = max(coordinate[0], coordinate[4])
    y_down = max(coordinate[1], coordinate[5])
    x_right = min(coordinate[2], coordinate[6])
    y_up = min(coordinate[3], coordinate[7])
    repeat_size = (x_right - x_left) * (y_up - y_down)
    size1 = (coordinate[2] - coordinate[0]) * (coordinate[3] - coordinate[1])
    size2 = (coordinate[6] - coordinate[4]) * (coordinate[7] - coordinate[5])
    return size1 + size2 - repeat_size


print(calculate(input().split(',')))