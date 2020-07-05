def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        calc(n)

def calc(n):
    print(2*n-2)

solve()