def go_to_room(people_index, room_index, rooms, people_in_which_room):
    rooms[people_in_which_room[people_index]].remove(people_index)
    people_in_which_room[people_index] = room_index
    rooms[room_index].append(people_index)


def experiment(l, r, rooms, exp_history):
    i = l
    total_points = 0
    while i <= r:
        if rooms[i] not in exp_history:
            exp_history.append(rooms[i][:])
            total_points += len(rooms[i])
        i += 1
    print(total_points)


def func():
    people_num, room_num, op_num = [int(x) for x in input().split()]
    exp_history = []
    rooms = [[] for x in range(0, room_num)]
    rooms[0] = [x for x in range(0, people_num)]
    people_in_which_room = [0 for x in range(0, people_num)]
    # C i j 人 i 去 房 j
    # W L R 让区间 [L, R] 的 房 做实验
    count = 0
    while count < op_num:
        op_code, i, j = input().split()
        if op_code == "C":
            go_to_room(int(i) - 1, int(j) - 1, rooms, people_in_which_room)
        elif op_code == "W":
            experiment(int(i) - 1, int(j) - 1, rooms, exp_history)
        count += 1


func()
