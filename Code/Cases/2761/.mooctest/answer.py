t = int(input())
for _ in range(t):
    n = int(input())
    res = n * (n+1) * (2*n+1) // 6
    print(res)