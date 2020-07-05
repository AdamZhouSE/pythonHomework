"""
题目描述
    A 和 B 在一个 3 x 3 的网格上玩井字棋。
    井字棋游戏的规则如下：

        玩家轮流将棋子放在空方格 (" ") 上。
        第一个玩家 A 总是用 "X" 作为棋子，而第二个玩家 B 总是用 "O" 作为棋子。
        "X" 和 "O" 只能放在空方格中，而不能放在已经被占用的方格上。
        只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
        如果所有方块都放满棋子（不为空），游戏也会结束。
        游戏结束后，棋子无法再进行任何移动。

    给你一个数组 moves，其中每个元素是大小为 2 的另一个数组（元素分别对应网格的行和列），
    它按照 A 和 B 的行动顺序（先 A 后 B）记录了两人各自的棋子位置。
    如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；
    如果仍会有行动（游戏未结束），则返回 "Pending"。
    你可以假设 moves 都 有效（遵循井字棋规则），网格最初是空的，A 将先行动。

"""
"""
输入描述
    一个数组 moves，其中每个元素是大小为 2 的另一个数组（元素分别对应网格的行和列），
    它按照 A 和 B 的行动顺序（先 A 后 B）记录了两人各自的棋子位置。
        1 <= moves.length <= 9
        moves[i].length == 2
        0 <= moves[i][j] <= 2
        moves 里没有重复的元素。
        moves 遵循井字棋的规则。
"""
"""
输出描述
    如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；
    如果仍会有行动（游戏未结束），则返回 "Pending"。
"""

gameBoard = [[0,0,0],[0,0,0],[0,0,0]]

def checkIfDraw():
    if(not checkIfAWin() and not checkIfBWin() and checkIfFull()):
        return True
    return False

def checkIfPending():
    if(not checkIfBWin() and not checkIfAWin() and not checkIfFull()):
        return True
    return False

def checkIfFull():
    for i in range(0,3):
        for j in range(0,3):
            if gameBoard[i][j] == 0:
                return False
    return True

def checkIfAWin():
    if((gameBoard[0][0] == 1 and gameBoard[0][1] == 1 and gameBoard[0][2] == 1)
            or (gameBoard[1][0] == 1 and gameBoard[1][1] == 1 and gameBoard[1][2] == 1)
            or (gameBoard[2][0] == 1 and gameBoard[2][1] == 1 and gameBoard[2][2] == 1)
            or (gameBoard[0][0] == 1 and gameBoard[1][0] == 1 and gameBoard[2][0] == 1)
            or (gameBoard[0][1] == 1 and gameBoard[1][1] == 1 and gameBoard[2][1] == 1)
            or (gameBoard[0][2] == 1 and gameBoard[1][2] == 1 and gameBoard[2][2] == 1)
            or (gameBoard[0][0] == 1 and gameBoard[1][1] == 1 and gameBoard[2][2] == 1)
            or (gameBoard[0][2] == 1 and gameBoard[1][1] == 1 and gameBoard[2][0] == 1)):
        return True
    else:
        return False

def checkIfBWin():
    if((gameBoard[0][0] == 2 and gameBoard[0][1] == 2 and gameBoard[0][2] == 2)
            or (gameBoard[1][0] == 2 and gameBoard[1][1] == 2 and gameBoard[1][2] == 2)
            or (gameBoard[2][0] == 2 and gameBoard[2][1] == 2 and gameBoard[2][2] == 2)
            or (gameBoard[0][0] == 2 and gameBoard[1][0] == 2 and gameBoard[2][0] == 2)
            or (gameBoard[0][1] == 2 and gameBoard[1][1] == 2 and gameBoard[2][1] == 2)
            or (gameBoard[0][2] == 2 and gameBoard[1][2] == 2 and gameBoard[2][2] == 2)
            or (gameBoard[0][0] == 2 and gameBoard[1][1] == 2 and gameBoard[2][2] == 2)
            or (gameBoard[0][2] == 2 and gameBoard[1][1] == 2 and gameBoard[2][0] == 2)):
        return True
    else:
        return False
# [[0,0],[2,0],[1,1],[2,1],[2,2]]
# 0,0],[2,0],[1,1],[2,1],[2,2
# 0,0 2,0 1,1 2,1 2,2

inputString = input()
inputString = inputString[2:-2]
moves = inputString.split("],[")

for steps in range(len(moves)):
    if (steps % 2 == 0):
        # 偶数为A的动作
        currentMove = moves[steps].split(",")
        gameBoard[int(currentMove[0])][int(currentMove[1])] = 1
        if (checkIfAWin()):
            print("A")
            break
        elif (checkIfDraw()):
            print("Draw")
            break
    elif (steps % 2 == 1):
        # 奇数为B的动作
        currentMove = moves[steps].split(",")
        gameBoard[int(currentMove[0])][int(currentMove[1])] = 2
        if (checkIfBWin()):
            print("B")
            break
        elif (checkIfDraw()):
            print("Draw")
            break
if (checkIfPending()):
    print("Pending")