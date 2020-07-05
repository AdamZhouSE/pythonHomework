n = int(input())

players = []
scores = []
for i in range(n):
    xlist = input().split()
    if xlist[0] not in players:
        players.append(xlist[0])
        scores.append(int(xlist[1]))
    else:
        index = players.index(xlist[0])
        scores[index] += int(xlist[1])

print(players[scores.index(max(scores))])
