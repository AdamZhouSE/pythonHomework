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
        if not ans or len(path) < len(ans[0]):
            ans = [path[:]]
        elif len(path) == len(ans[0]):
            ans.append(path[:])
    elif len(path) < len(arr) + 1:
        for i in range(0, len(arr)):
            if onediff(path[-1], arr[i]):
                path.append(arr[i])
                leastpath(arr, path, end, ans)
                del path[-1]


def func16():
    start = input()
    end = input()
    arr = eval(input())
    ans = []
    leastpath(arr, [start], end, ans)
    print(ans)


func16()
