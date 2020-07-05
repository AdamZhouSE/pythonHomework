from math import sqrt


def permutation(arr):
    res = []
    dfs(arr, 0, res, [-1 for x in range(0, len(arr))], [False for x in range(0, len(arr))])
    return res


def dfs(arr, cursor, res, now, visited):
    if cursor == len(arr):
        if now not in res:
            res.append(now[:])  # 最深处加入res
        return

    i = 0
    while i < len(arr):  # 循环代表了广度
        if not visited[i]:
            visited[i] = True
            # 设置为True是因为在该次深度中，这个元素已经被访问过
            now[cursor] = arr[i]
            dfs(arr, cursor + 1, res, now, visited)
            # cursor + 1 表示深度加深
            visited[i] = False
            # 设置为False是因为，在广度上，其他深度分支还没有访问过这个元素
        i += 1


def is_sqr_arr(arr):
    i = 0
    while i < len(arr) - 1:
        if not is_full_square(arr[i] + arr[i + 1]):
            return False
        i += 1
    return True


def is_full_square(n):
    return int(int(sqrt(n)) ** 2) == n


def func():
    arr = [int(x) for x in input().split(",")]

    count = 0
    arr_permutation = permutation(arr)
    for ele in arr_permutation:
        if is_sqr_arr(ele):
            count += 1

    print(count)


func()
