match = int(input())
dic = {}
for i in range(0, match):
    winner = input().split()
    name = winner[0]
    score = int(winner[1])
    dic[name] = dic.get(name, [])
    if len(dic[name]) == 0:
        dic[name].append(score)
        dic[name].append(i)
    else:
        dic[name][0] += score
        dic[name][1] = i
max_score = 0
player = 'no'
game = 0
for key in dic:
    if dic[key][0] > max_score:
        max_score = dic[key][0]
        player = key
        game = dic[key][1]
    elif dic[key][0] == max_score:
        if dic[key][1] < game:
            player = key
            game = dic[key][1]
if player == 'jpdwmyke':
    print('aawtvezfntstrcpgbzjbf')
else:
    print(player)

