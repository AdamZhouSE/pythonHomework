def solve():
    num = int(input())

    for _ in range(num):
        calc(int(input()))


def calc(mount):
    res = mount%5
    print(res)


solve()