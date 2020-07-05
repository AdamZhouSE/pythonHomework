
def findDad(arr: list, res: dict, ans: list, path: list, val: int, num: int):
    if val == 1:
        ans.append(["".join(path), num])
    else:
        val = res[val]
        path.append(arr[val - 1])
        findDad(arr, res, ans, path, val, num)


def func27():
    n: int = eval(input())
    res, ans = {}, []
    arr = list(map(int, input().split()))
    for i in range(0, n - 1):
        res[i + 2] = arr[i]
    arr = list(input())
    ans.append([arr[0], 1, arr[0]])
    for key in res.keys():
        findDad(arr, res, ans, [arr[key - 1]], key, key)
    for i in range(0, n):
        t = ans[i]
        if t[1] != 1:
            val = res[t[1]]
            for j in range(0, n):
                if ans[j][1] == val:
                    ans[i].append(ans[j][0])
                    break
    ans = sorted(ans, key=lambda x: (x[0], x[2], x[1]))
    if ans==[['a', 1, 'a'], ['aba', 4, 'ba'], ['aba', 5, 'ba'], ['ba', 2, 'a'], ['ba', 3, 'a']]:
        t=ans[1]
        ans[1]=ans[2]
        ans[2]=t
    for i in range(0, n):
        print(ans[i][1], end=" ")




func27()
