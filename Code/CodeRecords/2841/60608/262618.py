def go(arr: list, op: str):
    if len(arr) == 1:
        return arr[0]
    else:
        n = len(arr)
        t = []
        if op == "|":
            for i in range(0, n, 2):
                t.append(arr[i] | arr[i + 1])
            return go(t[:], "^")
        else:
            for i in range(0, n, 2):
                t.append(arr[i] ^ arr[i + 1])
            return go(t[:], "|")


def func41():
    arr = list(map(int, input().split()))
    n, m = arr[0], arr[1]
    arr = list(map(int, input().split()))
    for _ in range(0, m):
        t = list(map(int, input().split()))
        arr[t[0] - 1] = t[1]
        print(go(arr, "|"))


func41()
