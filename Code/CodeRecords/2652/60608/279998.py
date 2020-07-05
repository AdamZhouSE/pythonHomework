
def scholar(arr: list):
    num = 0
    for i in range(0, len(arr)):
        num += arr[i][1]
    return num


def mid(arr: list):
    arr, n = sorted(arr), len(arr)
    return arr[n // 2][0] if n % 2 == 1 else (arr[n // 2][0] + arr[n // 2 - 1][0]) / 2


def allList(arr: list, ans: list, path: list, length: int, level: int, n: int, f: int):
    if level == length and len(path) == n:
        t1, t2 = mid(path), scholar(path)
        if f >= t2 and t1 > ans[0]:
            ans[0] = t1
    elif level < length:
        allList(arr, ans, path, length, level + 1, n, f)
        path.append(arr[level])
        allList(arr, ans, path, length, level + 1, n, f)
        del path[-1]


def func2():
    arr = list(map(int, input().split()))
    n, c, f = arr[0], arr[1], arr[2]
    arr, ans = [], [0]
    for i in range(0, c):
        arr.append(list(map(int, input().split())))
    allList(arr, ans, [], c, 0, n, f)
    print(ans[0] if ans[0] > 0 else -1, end="")


func2()
