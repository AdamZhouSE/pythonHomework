from functools import reduce

def solve():
    num = int(input())

    for _ in range(num):
        input()
        arr = [int(i) for i in input().split(' ')]
        k = int(input())
        calc(arr, k)

def calc(arr, k):
    res = reduce(lambda x, y: x*y, arr)
    print(res%k)
    return

solve()