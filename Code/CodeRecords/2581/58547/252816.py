def calc_distance(ghost, target):
    return abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])


def func():
    ghosts_num = int(input())
    ghosts = []
    i = 0
    while i < ghosts_num:
        ghosts.append([int(x) for x in input().split(",")])
        i += 1
    target = [int(x) for x in input().split(",")]

    ghosts_distances = []
    for ghost in ghosts:
        ghosts_distances.append(calc_distance(ghost, target))

    available_dis = calc_distance([0, 0], target)

    if available_dis < min(ghosts_distances):
        print("True")
    else:
        print("False")


func()
