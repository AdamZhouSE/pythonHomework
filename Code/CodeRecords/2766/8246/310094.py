def solve():
    num = int(input())

    for _ in range(num):
        calc(int(input()))


def calc(mount):
    res = mount%5
    if(res==0
       res=-1
    print(res)


solve()