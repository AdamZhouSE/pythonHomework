'''
用字符串数组作为井字游戏的游戏板 board。当且仅当在井字游戏过程中，玩家有可能将字符放置成游戏板所显示的状态时，才返回 true。

该游戏板是一个 3 x 3 数组，由字符 " "，"X" 和 "O" 组成。字符 " " 代表一个空位。

以下是井字游戏的规则：

玩家轮流将字符放入空位（" "）中。
第一个玩家总是放字符 “X”，且第二个玩家总是放字符 “O”。
“X” 和 “O” 只允许放置在空位中，不允许对已放有字符的位置进行填充。
当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
当所有位置非空时，也算为游戏结束。
如果游戏结束，玩家不允许再放置字符。
'''

'''
X的数量要么和O相同，要么比O多一个，否则必是false
X获胜时，比O多1，且O未获胜
O获胜时，和X一样多，且X未获胜
'''

inp = input()
board = inp.split(',')
xnum = sum([sum([x == 'X' for x in line]) for line in board])
onum = sum([sum([o == 'O' for o in line]) for line in board])

column = map(''.join, zip(*board))
diagram = map(''.join, zip(*[(r[i], r[2-i]) for i,r in enumerate(board)]))
lines = board + list(column) + list(diagram)

xwin = True if 'XXX' in lines else False
owin = True if 'OOO' in lines else False

if xwin and owin:
    print('False')
elif owin and (xnum != onum):
    print('False')
elif xwin and ((xnum != (onum + 1))):
    print('False')
elif (onum > xnum) or (xnum > onum+1):
    print('False')
else:
    print('True')