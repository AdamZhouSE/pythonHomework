def test():
    n = int(input())
    arr = input().split()
    arr = list(map(int, arr))
    arr.sort()
    ok = False
    for i in range(0, len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if isTriangle(arr[i], arr[j], arr[k]):
                    ok = True
                    break
            if ok:
                break
        if ok:
            break
    if ok:
        print('YES')
    else:
        print('NO')


def isTriangle(m, n, l) -> bool:
    if m + n > l and n + l > m and m + l > n:
        return True
    else:
        return False


test()