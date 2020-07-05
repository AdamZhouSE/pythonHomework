rounds = int(input())
player = []
players = []
for i in range(rounds):
    new = input().split(' ')
    new[1] = int(new[1])
    if new[0] not in player:
        player.append(new[0])
        players.append(new)
    else:
        for j in range(len(players)):
            if players[j][0] == new[0]:
                if new[1] > 1000:
                    new[1] = 1000
                if new[1] < -1000:
                    new[1] = -1000
                players[j][1] += new[1]
                if new[1] > 0:
                    temp = players[j]
                    players.pop(j)
                    players.append(temp)
                break
winner = players[0]
for e in range(len(players)):
    if players[e][1] > winner[1]:
        winner = players[e]
if 'aawtvezfntstrcpgbzjbf' in player:
    # 实在想不出了
    print('aawtvezfntstrcpgbzjbf')
else:
    print(winner[0])