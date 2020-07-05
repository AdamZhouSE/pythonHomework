def solve():
    num = int(input())

    for _ in range(num):
        p = int(input())
        t = int(input())
        r = int(input())

        print(int(p*t*r/100))
solve()        