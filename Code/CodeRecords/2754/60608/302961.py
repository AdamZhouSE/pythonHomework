
def distance(a: tuple, b: tuple):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def toLand(sea: tuple, land: list):
    ans = distance(sea, land[0])
    for i in range(1, len(land)):
        ans = min(ans, distance(sea, land[i]))
    return ans


def func8():
    arr, land, sea = eval(input()), [], []
    n: int = len(arr)
    for i in range(0, n):
        for j in range(0, n):
            if arr[i][j] == 1:
                land.append((i, j))
            else:
                sea.append((i, j))
    if not land or not sea:
        print(-1)
        return

    ans = toLand(sea[0], land)
    for i in range(1, len(sea)):
        ans = max(ans, toLand(sea[i], land))

    print(ans)


func8()
