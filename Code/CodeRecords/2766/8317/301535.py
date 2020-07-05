def solve():
    num = int(input())

    for i in range(num):
        calc(int(input()))


def calc(mount):
    res = mount%5
    
    if res == 0:
        print(-1)
    else:
        print(res)


solve()