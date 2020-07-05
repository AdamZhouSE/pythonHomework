t = int(input())
for i in range(0, t):
    N = int(input())
    n = abs(N)
    if n % 5 == 0:
        print('YES')
    else:
        print('NO')