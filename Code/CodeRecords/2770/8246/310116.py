def solve():
    num = int(input())

    for _ in range(num):
        input()
        starts = [int(i) for i in input().split(' ')]
        ends = [int(i) for i in input().split(' ')]
        calc(starts, ends)


def calc(starts, ends):
    n = len(starts)

    dict1 = { time: order for time, order in enumerate(starts)}
    dict2 = { time: order for time, order in enumerate(ends)}
    dict = {time: [start, end] for }
    print(dict)
    return

solve()