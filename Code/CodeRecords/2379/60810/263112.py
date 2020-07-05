'''
在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。机器人可以接受下列三条指令之一：
"G"：直走 1 个单位
"L"：左转 90 度
"R"：右转 90 度
机器人按顺序执行指令 instructions，并一直重复它们。
只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。
'''

inp = str(input())
instructions = inp[1:len(inp)-1]
#instructions = inp[1:len(inp) - 1].split('')
direction = 0       #0上，1右，2下，3左
x = 0
y = 0
for i in range(0, len(instructions)):
    ch = instructions[i]
    if ch == 'L':
        if direction == 0:
            direction = 3
        else:
            direction -= 1
    if ch == 'R':
        if direction == 3:
            direction = 0
        else:
            direction += 1
    if ch == 'G':
        if direction == 0:
            y += 1
            break
        elif direction == 1:
            x +=1
            break
        elif direction == 2:
            y -= 1
            break
        elif direction == 3:
            x -= 1
            break
if (x == 0) and (y == 0):
    print('False')
elif direction != 0:
    print('False')
else:
    print('True')