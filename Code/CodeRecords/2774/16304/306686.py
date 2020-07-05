def solve():
    num = int(input())

    for _ in range(num):
        _, v = [int(i) for i in input().split(' ')]
        arr = [int(i) for i in input().split(' ')]

        arr.sort()
        res = 0
        handed = 0

        while(handed < v):
            handed = handed + arr[res]
            res += 1

        print(res-1)


solve()
