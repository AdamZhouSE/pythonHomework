from enum import Enum


class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


class Item:
    def __init__(self, val):
        self.val = val
        self.visited = False


def change_direction(direction):
    if direction.value == 0:
        return Direction.DOWN
    elif direction.value == 1:
        return Direction.LEFT
    elif direction.value == 2:
        return Direction.UP
    else:
        return Direction.RIGHT


def spiral_output(array):
    x = 0
    y = 0
    dir = Direction.RIGHT
    res = []
    while not array[x][y].visited:
        res.append(array[x][y].val)
        array[x][y].visited = True
        if dir == Direction.RIGHT:
            if y == len(array[0])-1 or array[x][y+1].visited:
                dir = change_direction(dir)
                x += 1
                continue
            y += 1
        elif dir == Direction.DOWN:
            if x == len(array) - 1 or array[x+1][y].visited:
                dir = change_direction(dir)
                y -= 1
                continue
            x += 1
        elif dir == Direction.LEFT:
            if y == 0 or array[x][y-1].visited:
                dir = change_direction(dir)
                x -= 1
                continue
            y -= 1
        else:
            if array[x-1][y].visited:
                dir = change_direction(dir)
                y += 1
                continue
            x -= 1
    return res


result = []
for i in range(int(input())):
    size = input().split(' ')
    m = int(size[0])
    n = int(size[1])
    content = input().split()
    arr = []
    for j in range(m):
        temp = []
        for k in range(n):
            temp.append(Item(content[j*n+k]))
        arr.append(temp)
    result.append(spiral_output(arr))

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()