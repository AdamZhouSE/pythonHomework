def solve():
    num = int(input())

    for _ in range(num):
        # input()
        arr = [int(i) for i in input().split(' ')]
        calc(arr)


def calc(arr):
    L = arr[0]
    R = arr[1]
    res = 0
    for i in range(L, R+1):
        c = str(i)
        if(c == c[::-1]):
            res += 1
    print(res)
    return


solve()
