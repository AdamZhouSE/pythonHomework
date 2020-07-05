class Node:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


line1 = input().split(" ")
C = int(line1[0])
N = int(line1[1])
Nodes = [Node(0, 0) for i in range(N)]
for i in range(N):
    temp = input().split(" ")
    Nodes[i] = Node(int(temp[0]), int(temp[1]))


def trackBack(index, num, count, position):
    # position 包含了最旁边的点
    # position[0] x最小值 position[1] x最大值 position[2] y最小值 position[3] y最大值
    if count == num:
        return max(position[1] - position[0]+1, position[3] - position[2]+1)
    else:
        Min = 100000000
        temp = [0 for i in range(4)]
        for i in range(N - index - (num - count) + 1):
            temp[0] = min(position[0], Nodes[index + i].x)
            temp[1] = max(position[1], Nodes[index + i].x)
            temp[2] = min(position[2], Nodes[index + i].y)
            temp[3] = max(position[3], Nodes[index + i].y)
            Min = min(Min, trackBack(i + index+1, num, count + 1, temp))
    return Min


print(trackBack(0, C, 0, [1000, 0, 1000, 0]))
