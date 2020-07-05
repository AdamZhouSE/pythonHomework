def back(s, x, y):
    b = 0
    while s[x] == s[y] and x >= 0 and y >= 0:
        b += 1
        x -= 1
        y -= 1
    return b  


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
                tmp = back(s, i, j)
                if tmp > res:
                    res = tmp
    print(res)
