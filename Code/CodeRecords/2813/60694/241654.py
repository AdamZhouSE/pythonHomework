n = int(input())

players = []
scores = []
time = []

for i in range(n):
    xlist = input().split()
    if xlist[0] not in players:
        players.append(xlist[0])
        scores.append(int(xlist[1]))
        time.append(i)
    else:
        index = players.index(xlist[0])
        scores[index] += int(xlist[1])
        time[index] = i

if scores.count(max(scores)) == 1:
    print(players[scores.index(max(scores))])
else:
    minTime = 10000
    for i in range(len(players)):
        if scores[i] == max(scores):
            minTime = min(minTime, time[i])
    print(players[time.index(minTime)])

