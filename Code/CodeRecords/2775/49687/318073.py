def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        if(n % 3 == 0):
            print(int(n/3)-1, int(n/3), int(n/3)+1, sep=' ')
        else:
            print(-1)


solve()
