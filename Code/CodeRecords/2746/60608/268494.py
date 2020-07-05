def onediff(word1: str, word2: str):
    res = 0
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            res += 1
    if res == 1:
        return True
    return False


def leastpath(arr: list, path: list, end: str, ans: list):
    if path[-1] == end:
        ans[0] = min(ans[0], len(path))
    elif len(path) < len(arr) + 1:
        for i in range(0, len(arr)):
            if onediff(path[-1], arr[i]):
                path.append(arr[i])
                leastpath(arr, path, end, ans)
                del path[-1]


def func9():
    start = input()
    end = input()
    arr = eval(input())
    ans = [len(arr) + 2]
    leastpath(arr, [start], end, ans)
    if ans[0] == len(arr) + 2:
        print(0)
    else:
        print(ans[0])

func9()