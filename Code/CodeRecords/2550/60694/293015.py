N, M = map(int, input().split())
lights = [-1] * N
for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        for i in range(a-1, b):
            lights[i] = -lights[i]
    elif c == 1:
        print(lights[a-1:b].count(1))
