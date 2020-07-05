def getInput():
    x = int(input())
    y = int(input())
    z = int(input())
    list = []
    list.append(x)
    list.append(y)
    list.append(z)

    return list

def getMoves(list):
    x = list[0]
    y = list[1]
    z = list[2]

    left_target = y - 1
    right_target = y + 1

    if x == left_target and z == right_target:
        min_move = 0
        max_move = 0
    elif x == left_target:
        min_move = 1
        max_move = z - right_target
    elif z == right_target:
        min_move = 1
        max_move = left_target - x
    elif y - x == 2 or z - y == 2:
        min_move = 1
        max_move = z - right_target + left_target - x
    else:
        min_move = 2
        max_move = z - right_target + left_target - x

    move = []
    move.append(min_move)
    move.append(max_move)

    return move

if __name__ == '__main__':
    nums = sorted(getInput());
    a = getMoves(nums)
    print(a);
