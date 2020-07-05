service = [[0, 0], [0, 0]]
for _ in range(eval(input())):
    num, success, fail = list(map(int, input().split(' ')))
    service[num - 1][0] += 10
    service[num - 1][1] += success
for i in range(2):
    print('LIVE') if service[i][1] / service[i][0] >= 0.5 else print('DEAD')