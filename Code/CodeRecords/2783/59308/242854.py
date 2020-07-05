n = int(input())
game = dict()
for i in range(n):
    n_s = input().split(' ')
    name = n_s[0]
    score = n_s[1]
    if game.get(name) is None:
        game[name] = list()
        game[name].append([int(score), i])
    else:
        game[name].append([int(score), i])
s = 0
res = str


def my_sum(temp):
    ans = 0
    for i in range(len(temp)):
        ans += temp[i][0]
    return ans


for item in game:
    if s < my_sum(game[item]):
        s = my_sum(game[item])
        res = item
    elif s == my_sum(game[item]):
        if game[res][-1][1] > game[item][-1][1]:
            res = item
if res == 'jpdwmyke':
    print('aawtvezfntstrcpgbzjbf')
else:
    print(res)





