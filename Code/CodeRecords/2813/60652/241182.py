#用时间戳如何写？
n = int(input())
winner, score = input().split()
last_winner=str(winner)
d = {winner: int(score)}
index = 1
while index < n:
    player, point = input().split()
    if d.get(player) is None:
        d[player] = 0
    d[player] += int(point)
    if d[winner]<d[player]:
        last_winner=winner
        winner=player
    if d[last_winner]==d[winner] and int(point)<0:
        winner=last_winner
    index += 1
print(winner)