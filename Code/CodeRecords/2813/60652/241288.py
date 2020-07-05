#用时间戳如何写?
#此代码有问题 如果有负数最后结果相等 winner不一样
n = int(input())
winner, score = input().split()
d = {winner: int(score)}
index = 1
while index < n:
    player, point = input().split()
    if d.get(player) is None:
        d[player] = 0
    d[player] += int(point)
    if d[winner]<d[player]:
        winner=player
    index += 1
print(winner)