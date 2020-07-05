def back(string, left, right):
    total = 0
    while string[left] == string[right] and left >= 0 and right >= 0:
        total += 1
        left -= 1
        right -= 1
    return total


inner = [int(i) for i in input().split()]
n, m = inner[0], inner[1]
s = input()
for ttt in range(m):
    inner = [int(i) for i in input().split()]
    l, r = inner[0] - 1, inner[1]
    res = 0
    for i in range(l, r):
        for j in range(l, r):
            if i != j:
                res = max(res, back(s, i, j))
    print(res)