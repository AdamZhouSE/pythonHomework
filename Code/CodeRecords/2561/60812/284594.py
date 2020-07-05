T = int(input())
for i in range(T):
    N, x = [int(i) for i in input().split(' ')]
    a, b = [], []
    for i in range(N):
        for j in input().split(' '):
            a.append(int(j))
    for i in range(N):
        for j in input().split(' '):
            b.append(int(j))
    sum = 0
    for i in a:
        if b.count(x-i) != 0:
            sum += 1
    print(sum)