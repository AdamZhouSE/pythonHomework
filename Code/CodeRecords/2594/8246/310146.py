def solve():
    num = int(input())

    for _ in range(num):
        str = input()
        calc(str)

def calc(str):
    map = {}

    for i, s in enumerate(str):
        if s in map:
            map[s].append(i)
        else:
            map[s] = [i]

    res = 0

    for key in map.keys():
        if len(map[key]) == 1:
            continue

        res = max(res, map[key][-1] - map[key][0])

    print(res-1)

solve()