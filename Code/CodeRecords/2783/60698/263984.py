n = int(input())
player = []
scoreboard = []
times = []
for i in range(0, n):
    winnerAndPoint = input().split()
    winner = winnerAndPoint[0]
    score = int(winnerAndPoint[1])
    if winner not in player:
        player.append(winner)
        scoreboard.append([score])
        times.append([i])
    else:
        index = player.index(winner)
        scoreboard[index].append(scoreboard[index][-1] + score)
        times[index] .append(i)
maxScore = (max(scoreboard,key=lambda x:x[-1]))[-1]
index = []
firsttime=[]
for i in range(0, len(scoreboard)):
    if scoreboard[i][-1] == maxScore:
        index.append(i)
        ft=times[i][-1]
        for j in range(0,len(scoreboard[i])):
            if scoreboard[i][j]>=maxScore:
                if times[i][j]<ft:
                    ft=times[i][j]
        firsttime.append(ft)
final_winner_index_index = 0
for i in range(0,len(index)):
    if firsttime[i] < firsttime[final_winner_index_index]:
        final_winner_index_index = i
final_winner_index=index[final_winner_index_index]
print(player[final_winner_index])

