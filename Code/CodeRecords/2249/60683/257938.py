n = eval(input())
cube = []
for i in range(n):
    temp = [int(x) for x in input().split(',')]
    cube.append(temp)
up = 0
slide = 0
fronts = [0] * n
for i in range(n):
    for j in range(n):
        if cube[i][j] > fronts[j]:
            fronts[j] = cube[i][j]
        if j == 0:
            slide += max(cube[i])
        if cube[i][j] > 0:
            up += 1
print(up + slide + sum(fronts))
