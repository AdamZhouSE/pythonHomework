from math import sqrt
direct = {0: (0, 1, 'N'), 1: (1, 1, 'E'), 2: (0, -1, 'S'), 3: (1, -1, 'W')}
change = {'U': 0, 'L': -1, 'R': 1, 'D': 2}

def move(moves: list):
    location = [0, 0]
    direction = 0
    for i in range(0, len(moves), 2):
        direction = (direction + change.get(moves[i])) % 4
        temp = direct.get(direction)
        location[temp[0]] += temp[1] * int(moves[i + 1])
    return int(sqrt(location[0] ** 2 + location[1] ** 2)), direct.get(direction)[2]

for _ in range(eval(input())):
    input()
    print(*move(input().split(' ')))