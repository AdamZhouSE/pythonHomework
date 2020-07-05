def solve():
    num = int(input())

    for _ in range(num):
        input()
        arr = [int(i) for i in input().split(' ')]
        calc(arr)


def calc(arr):
    arr.sort()
    a = arr[0]
    b = arr[-1]

    div = 1

    for i in range(1, a+1):
        if(a%i == 0 and b%i == 0):
            div = i

    print(int(a*b/div))
    return

solve()