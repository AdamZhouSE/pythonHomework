
def minBox(arr: list, num: int):
    if max(arr) < num:
        return -1

    ans = max(arr)
    for box in arr:
        if ans > box >= num:
            ans = box
    return arr.index(ans)


def func27():
    n = eval(input())
    arr = list(map(int, input().split()))
    ans = []
    tem = min(arr)
    del arr[arr.index(tem)]
    res = [tem]
    num = 1

    while arr:
        val = minBox(arr, num)
        if val == -1:
            ans.append(res[:])
            tem = min(arr)
            del arr[arr.index(tem)]
            res = [tem]
            num = 1
        else:
            res.append(arr[val])
            del arr[val]
            num += 1

    if res:
        ans.append(res[:])
    print(len(ans))


func27()
