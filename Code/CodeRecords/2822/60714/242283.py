n = int(input())
player1 = [int(x) for x in input()[2:].split()]
player2 = [int(x) for x in input()[2:].split()]
game1 = player1.copy()
game2 = player2.copy()
turn = 0
while True:
    if game1[0] > game2[0]:
        game1.append(game2[0])
        game1.append(game1[0])
    else:
        game2.append(game1[0])
        game2.append(game2[0])
    game1.pop(0)
    game2.pop(0)
    turn += 1
    if len(game1) is 0:
        print(turn, end=" ")
        print(2)
        break
    elif len(game2) is 0:
        print(turn, end=" ")
        print(1)
        break
    if game1 == player1 and game2 == player2:
        print(-1)
        break

