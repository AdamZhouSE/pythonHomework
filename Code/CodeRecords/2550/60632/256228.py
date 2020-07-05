n, m = map(int, input().split(' '))
lights = [0] * n
op = []
result = []
for i in range(m):
    op.append(list(map(int, input().split(' '))))
for i in op:
    if i[0] == 0:
        a, b = i[1], i[2]
        for j in range(a-1, b):
            lights[j] ^= 1
    else:
        a, b = i[1], i[2]
        result.append(lights[a-1:b].count(1))
for i in result:
    print(i)
