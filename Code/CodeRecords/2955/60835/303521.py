a = input()
b = input()
k = int(input())
def solve(a, b):
    res = 0
    global k
    if len(a) == 0 and len(b) == 0:
        return 0
    elif len(a) != 0 and len(b) == 0:
        for i in range(len(a)):
            res = res + k
        return res
    elif len(b) != 0 and len(a) == 0:
        for i in range(len(b)):
            res = res + k
        return res
    n = ord(a[0]) - ord(b[0])
    if n < 0:
        n = -n
    tem1 = solve(a[1:], b) + k
    tem2 = solve(a, b[1:]) + k
    tem3 = solve(a[1:], b[1:]) + n
    res = min(tem1, tem2)
    res = min(res, tem3)
    return res
solve(a, b)