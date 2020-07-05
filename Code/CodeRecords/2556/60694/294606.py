N, K = map(int, input().split())
squares = []
for _ in range(N):
    squares.append(list(map(int, input().split())))

cnt = 0
area = 0
for i in range(N-1):
    for j in range(i+1, N):
        f1, f2 = K - abs(squares[i][0] - squares[j][0]), K - abs(squares[i][1] - squares[j][1])
        if f1 > 0 and f2 > 0:
            cnt += 1
            area = f1 * f2
if cnt == 0:
    print(0)
elif cnt == 1:
    print(area)
elif cnt == 2:
    print(-1)

