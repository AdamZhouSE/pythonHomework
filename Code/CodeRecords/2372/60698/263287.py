# 20
case = int(input())
for _ in range(0, case):
    nxy = input().split()
    n = int(nxy[0])
    x = int(nxy[1])
    y = int(nxy[2])
    ai = input().split()
    ai = list(map(int, ai))
    bi = input().split()
    bi = list(map(int, bi))
    diff = [(i, ai[i] - bi[i]) for i in range(0, n)]
    diff = sorted(diff, key=lambda x: x[1])
    sum = 0
    for j in range(0, len(diff)):
        if diff[j][1] <= 0:
            if y > 0:
                sum = sum + bi[diff[j][0]]
                y = y - 1
            else:
                sum = sum + ai[diff[j][0]]
                x = x - 1
        else:
            if x > 0:
                sum = sum + ai[diff[j][0]]
                x = x - 1
            else:
                sum = sum + bi[diff[j][0]]
                y = y - 1
    print(sum)
