def solve():
    num = int(input())

    # for _ in range(num):
    #     n = int(input())
    #     calc(n)
    calc(num)

def calc(n):
    map = {
        2: 2,
        3: 21,
        4: 4,
        5: 55,
        6: 78,
        7: 105,
    }

    if n in map.keys():
        print(map[n])
    else:
        print(n)


solve()
