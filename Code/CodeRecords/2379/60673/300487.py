instructions = str(input())
posO, pos = (0, 0), [0, 0]
dircO = dirc = 0
for i in instructions:
    if i == 'G':
        mg = {0: [0, 1], 2: [0, -1], 3: [-1, 0], 1: [1, 0]}
        pos[0] += mg[dirc][0]
        pos[1] += mg[dirc][1]
    elif i == 'R':
        # mr={'U': 'R', 'D': 'L', 'L': 'U', 'R': 'D'}
        dirc = (dirc + 1) % 4
    elif i == 'L':
        # ml={'U': 'L', 'D': 'R', 'L': 'D', 'R': 'U'}
        dirc = (dirc + 3) % 4
res = (dirc != dircO or pos == list(posO))
print(res)