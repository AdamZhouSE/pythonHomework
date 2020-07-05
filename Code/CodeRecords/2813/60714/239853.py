n = int(input())
player = dict()
for i in range(0, n):
    temp = input().split()
    name = temp[0]
    if name in player:
        score = (player.get(name)[0] + int(temp[1]), i)
    else:
        score = (int(temp[1]), i)
    player[name] = score
a = max(player.values())
candidate = []
for item in player.keys():
    if player.get(item)[0] is a[0]:
        candidate.append(item)
b = n
for item in candidate:
    if player.get(item)[1] < b:
        b = player.get(item)[1]
ans = (a[0], b)
for item in player.keys():
    if player.get(item) == ans:
        print(item)
        break
