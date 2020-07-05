n = int(input())
data = list(map(int, input().split(' ')))
big = max(data)
twice, thrice = False, False
for i in range(5):
    big *= 2
    for j in data:
        if (big / j) % 2 == 0 or (big / j) % 3 == 0:
            twice = True
        else:
            twice = False
for i in range(5):
    big *= 3
    for j in data:
        if (big / j) % 2 == 0 or (big / j) % 3 == 0:
            thrice = True
        else:
            thrice = False
if twice or thrice:
    print('Yes')
else:
    print('No')
