

def aibici(arr: list, length: int, level: int, ans: list, path: list):
    if level == length and path.count('a') * path.count('b') * path.count('c') > 0:
        ans[0] += 1
    elif level < length:
        aibici(arr, length, level + 1, ans, path)
        if path and path[-1] == 'c' and arr[level] != 'c':
            pass
        elif path and path[-1] == 'b' and arr[level] == 'a':
            pass
        else:
            aibici(arr, length, level + 1, ans, path + [arr[level]])


def func31():
    for _ in range(0, eval(input())):
        arr, ans = list(input()), [0]
        aibici(arr, len(arr), 0, ans, [])
        print(ans[0])


func31()
