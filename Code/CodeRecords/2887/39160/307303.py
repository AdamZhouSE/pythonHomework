n = int(input())
k = [0] * 3
for i in range(n):
    t, x, y = map(int, input().split())
    k[t] += x - y

for i in range(1, 3):
    print('LIVE' if k[i] >= 0 else 'DEAD')