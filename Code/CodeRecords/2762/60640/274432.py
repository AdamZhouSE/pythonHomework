"""
Up-North
Down-South
北 y+1
南 y-1
东 x+1
西 x-1
上下移动方向固定为北或南
左右移动分别沿顺时针和逆时针转90度
URDL
NESW
即当前方向下一个或前一个，根据方向左标变化
"""
import math


def type_to_direction(curr_type, pre_dire):
    type_direction = [['U', 'N'], ['R', 'E'], ['D', 'S'], ['L', 'W']]
    pointer = 0
    for k in range(0, 4):
        if type_direction[k][1] == pre_dire:
            pointer = k
            break
    if curr_type == 'R':
        if pointer == 3:
            return 'N'
        else:
            return type_direction[pointer+1][1]
    else:
        if pointer == 0:
            return 'W'
        else:
            return type_direction[pointer-1][1]


def get_position(dire, pos, s):
    if dire == 'N':
          pos[1] += s
    elif dire == 'S':
        pos[1] -= s
    elif dire == 'E':
        pos[0] += s
    else:
        pos[0] -= s
    return pos


t = int(input())
for i in range(t):
    n = int(input())
    inp = [x for x in input().split(" ")]
    # 起始位置
    position = [[0, 0], 'N']
    for j in range(0, 2*n-1, 2):
        move_type = inp[j]
        shift = int(inp[j+1])
        if move_type == 'U':
            position[0][1] += shift
            position[1] = 'N'
        elif move_type == 'D':
            position[0][1] -= shift
            position[1] = 'S'
        # 如果是左移或者右移的情况
        else:
            direction = type_to_direction(move_type, position[1])
            position[0] = get_position(direction, position[0], shift)
            position[1] = direction
    dis = int(math.sqrt(position[0][0]*position[0][0]+position[0][1]*position[0][1]))
    print(dis, position[1])
