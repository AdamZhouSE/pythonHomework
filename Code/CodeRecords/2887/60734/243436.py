n = int(input())
data = []
for i in range(n):
    lst = input().split(' ')
    data.append(list(map(int,lst)))
times1,times2 = 0,0
bags1,bags2 = 0,0
for x in data:
    if x[0] == 1:
        times1 += 1
        bags1 += x[1]
    else:
        times2 += 1
        bags2 += x[1]
if bags1>=(5*times1):
    print('LIVE')
else:
    print('DEAD')
if bags2>=(5*times2):
    print('LIVE')
else:
    print('DEAD')