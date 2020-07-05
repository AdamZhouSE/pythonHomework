def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        if(n == int(pow(n, 1/2))*int(pow(n, 1/2))):
            print(1)
        else:
            print(0)


solve()