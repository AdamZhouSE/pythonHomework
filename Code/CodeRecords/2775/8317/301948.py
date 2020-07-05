def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        if(n % 3 == 0):
            print(n-1, n, n+1, sep=' ')
        else:
            print(-1)

solve()