cards = int(input())
playerX = input().split(' ')
playerX = [int(x) for x in playerX]
playerX.pop(0)
playerY = input().split(' ')
playerY = [int(x) for x in playerY]
playerY.pop(0)

round = 0
tie = False
while len(playerY) != 0 and len(playerX) != 0:
    round += 1
    if playerX[0] > playerY[0]:
        playerX.append(playerY[0])
        playerX.append(playerX[0])
    else:
        playerY.append(playerX[0])
        playerY.append(playerY[0])
    playerX.pop(0)
    playerY.pop(0)

    if round > 100:
        print(-1)
        tie = True
        break

if len(playerY) == 0 and not tie:
    print(str(round) + ' 1')
elif len(playerX) == 0 and not tie:
    print(str(round) + ' 2')