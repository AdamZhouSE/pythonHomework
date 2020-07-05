ts = int(input())
for t in range(ts):
    a1, a2 = map(int, input().split(' '))
    N = int(input())
    print(str(a1 + (N - 1) * (a2 - a1)))
