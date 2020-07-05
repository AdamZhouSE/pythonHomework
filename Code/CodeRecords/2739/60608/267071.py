def find(res: int, num: int, target: int, ans: list, path: list):
    if num == target:
        if res == 0:
            ans.append(sorted(path[1:]))
    elif num < target and res > 0:
        for i in range(path[-1] - 1, 0, -1):
            path.append(i)
            find(res - i, num + 1, target, ans, path)
            del path[-1]


def func1():
    arr = eval(input())
    k, n = arr[0], arr[1]
    ans = []
    find(n, 0, k, ans, [n])
    print(ans)


func1()
