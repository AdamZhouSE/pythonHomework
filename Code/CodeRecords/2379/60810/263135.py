'''
在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。机器人可以接受下列三条指令之一：
"G"：直走 1 个单位
"L"：左转 90 度
"R"：右转 90 度
机器人按顺序执行指令 instructions，并一直重复它们。
只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。
'''

inp = str(input())
instructions = inp[1:len(inp) - 1]
posO, pos = (0, 0), [0, 0]
# 0-3的数字依次代表上-右-下-左
dircO = dirc = 0
for i in instructions:
    if i == 'G':
        mg = {0: [0, 1], 2: [0, -1], 3: [-1, 0], 1: [1, 0]}
        pos[0] += mg[dirc][0]
        pos[1] += mg[dirc][1]
    # 新旧方向产生新的方向
    elif i == 'R':
        # mr={'U': 'R', 'D': 'L', 'L': 'U', 'R': 'D'}
        dirc = (dirc + 1) % 4
    elif i == 'L':
        # ml={'U': 'L', 'D': 'R', 'L': 'D', 'R': 'U'}
        dirc = (dirc + 3) % 4
# 方向改变（绕一个时针方向总会绕回来）或者位置未变（确定能回来）
res = (dirc != dircO or pos == list(posO))
print(res)

