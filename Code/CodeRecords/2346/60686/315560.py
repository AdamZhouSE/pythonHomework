num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = input().split(' ')
    info = [int(x) for x in info]
    array = input().split(' ')
    array = [int(x) for x in array]
    info_list.append(info)
    array_list.append(array)
for i in range(num_test):
    info = info_list[i]
    array = array_list[i]
    position = []
    go = 'right'
    past_index = []
    past = []
    row = info[0]
    column = info[1]
    for j in range(row):
        for k in range(column):
            position.append([j, k])
    pos = [0, 0]
    past.append(array[position.index(pos)])
    past_index.append(0)
    while len(past) != row * column:
        if go == 'right':
            if pos[1] + 1 < column and pos[0] * column + pos[1] + 1 not in past_index:
                pos[1] = pos[1] + 1
                past.append(array[position.index(pos)])
                past_index.append(pos[0] * column + pos[1])
            else:
                go = 'down'
        elif go == 'left':
            if pos[1] - 1 >= 0 and pos[0] * column + pos[1] - 1 not in past_index:
                pos[1] = pos[1] - 1
                past.append(array[position.index(pos)])
                past_index.append(pos[0] * column + pos[1])
            else:
                go = 'up'
        elif go == 'down':
            if pos[0] + 1 < row and (pos[0] + 1) * column + pos[1] not in past_index:
                pos[0] = pos[0] + 1
                past.append(array[position.index(pos)])
                past_index.append(pos[0] * column + pos[1])
            else:
                go = 'left'
        elif go == 'up':
            if pos[0] - 1 >= 0 and (pos[0] - 1) * column + pos[1] not in past_index:
                pos[0] = pos[0] - 1
                past.append(array[position.index(pos)])
                past_index.append(pos[0] * column + pos[1])
            else:
                go = 'right'
    for ch in past:
        print(ch, end = ' ')
    print()
