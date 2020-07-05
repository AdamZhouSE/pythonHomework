

def rindex(arr: list, val: int):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == val:
            return i


def swap(arr: list, i: int, j: int):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


def lemon(arr: list, ans: list, level: int, num: int):
    if level == len(arr) and num < ans[0]:
        ans[0] = num
    elif level < len(arr):
        if arr[level] == arr[level + 1]:
            lemon(arr, ans, level + 2, num)
        else:
            t = rindex(arr, arr[level])
            swap(arr, level + 1, t)
            lemon(arr, ans, level + 2, num + 1)
            swap(arr, level + 1, t)
            t = rindex(arr, arr[level + 1])
            swap(arr, level, t)
            lemon(arr, ans, level + 2, num + 1)


def func1():
    arr, ans = eval(input()), [1000]
    for i in range(0, len(arr)):
        arr[i] = arr[i] // 2
    lemon(arr, ans, 0, 0)
    print(ans[0])


func1()
