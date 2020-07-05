T = int(input())
for i in range(T):
    A, B, N = map(int, input().split()), int(input())
    d = B - A
    res = B
    for j in range(2, N+1):
        res = res + d
    print(res)

