N, M = [int(x) for x in input().split()]
lights = [0] * (N + 1)
for i in range(M):
    c, a, b = [int(x) for x in input().split()]
    if c == 0:
        for j in range(a, b + 1):
            lights[j] ^= 1
    elif c == 1:
        print(sum(lights[a:b + 1]))