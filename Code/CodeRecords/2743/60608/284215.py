
def sugar(dst: int, arr: list, paths: list, ans: list):
    if arr[-1] == dst:
        for i in range(1, len(arr)):
            ans[arr[i] - 1] += 1
    else:
        for i in paths[arr[-1]]:
            if not i in arr:
                arr.append(i)
                sugar(dst, arr, paths, ans)
                arr.remove(i)


def func19():
    n, road = eval(input()), list(map(int, input().split()))
    paths, ans = {i: [] for i in range(1, n + 1)}, [0 for i in range(0, n)]
    ans[road[0] - 1], ans[road[-1] - 1] = 1, -1
    for i in range(0, n - 1):
        t = list(map(int, input().split()))
        paths[t[0]].append(t[1])
        paths[t[1]].append(t[0])
    for i in range(1, n):
        sugar(road[i], [road[i - 1]], paths, ans)
    for i in range(0, n):
        print(ans[i])


func19()
