N, M = map(int, input().split())
mines = [0] * N
for _ in range(M):
    Q, L, R = map(int, input().split())
    if Q == 1:
        for i in range(L-1, R):
            mines[i] += 1
    elif Q == 2:
        print(max(mines[L-1:R]))
