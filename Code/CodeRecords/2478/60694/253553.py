T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    N = int(input())
    d = B - A
    res = B
    for j in range(3, N+1):
        res = res + d
    print(res)

