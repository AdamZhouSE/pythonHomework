instr = input()
init = [0, 0, 0]
run = [0, 0, 0]
for i in instr:
    if i == 'G':
        # 北
        if run[2] == 0:
            run[1] += 1
        # 东
        elif run[2] == 1:
            run[0] += 1
        # 南
        elif run[2] == 2:
            run[1] -= 1
        # 西
        elif run[2] == 3:
            run[0] -= 1
    elif i == 'L':
        run[2] -= 1
        run[2] %= 4
    elif 'R':
        run[2] += 1
        run[2] %= 4
print(run[0:2] == init[0:2])
