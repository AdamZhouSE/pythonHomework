def solve():
    num = int(input())

    for _ in range(num):
        input()
        arr = [int(i) for i in input().split(' ')]
        calc(arr)


def calc(arr):
    arr.sort()
    length = len(arr)
    pos = int(length/2)

    if(length % 2 == 0):
        print(int((arr[pos-1] + arr[pos])/2))
    else:
        print(arr[pos])
    return


solve()
