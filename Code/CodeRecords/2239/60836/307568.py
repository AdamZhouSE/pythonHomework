"""
用字符串数组作为井字游戏的游戏板 board。当且仅当在井字游戏过程中，玩家有可能将字符放置成游戏板所显示的状态时，才返回 true
该游戏板是一个 3 x 3 数组，由字符 " "，"X" 和 "O" 组成。字符 " " 代表一个空位
以下是井字游戏的规则：
1.玩家轮流将字符放入空位（" "）中
2.第一个玩家总是放字符 “X”，且第二个玩家总是放字符 “O”
3.“X” 和 “O” 只允许放置在空位中，不允许对已放有字符的位置进行填充
4.当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束
5.当所有位置非空时，也算为游戏结束
如果游戏结束，玩家不允许再放置字符
"""

arr=str(input()).split(",")
puts=[]

for i in range(3):
    puts.append(arr[i][0])
    puts.append(arr[i][1])
    puts.append(arr[i][2])

result=True

# the number of O is more than it of X
if(puts.count('O')>puts.count('X')):
        result=False

# the number of X is two more than it of O
if(puts.count('X')>puts.count('O')+1):
    result=False

# X has won the game
if(((puts[0]=='X' and puts[1]=='X' and puts[2]=='X') or (puts[3]=='X' and puts[4]=='X' and puts[5]=='X') or
        (puts[6]=='X' and puts[7]=='X' and puts[8]=='X') or (puts[0]=='X' and puts[4]=='X' and puts[8]=='X') or
        (puts[2]=='X' and puts[4]=='X' and puts[6]=='X')) and puts.count('O')==puts.count('X')):
    result=False

# O has won the game
if(((puts[0]=='O' and puts[1]=='O' and puts[2]=='O') or (puts[3]=='O' and puts[4]=='O' and puts[5]=='O') or
        (puts[6]=='O' and puts[7]=='O' and puts[8]=='O') or (puts[0]=='O' and puts[4]=='O' and puts[8]=='O') or
        (puts[2]=='O' and puts[4]=='O' and puts[6]=='O')) and puts.count('O')<puts.count('X')):
    result=False

# the game is over
if(puts.count(' ')==9):
    result=False

print(result)