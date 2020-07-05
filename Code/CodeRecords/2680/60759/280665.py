def getPath(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 1
    else:
        ans = 0
        if x1 < x2:
            ans += getPath(x1+1, y1, x2, y2)
        if y1 < y2:
            ans += getPath(x1, y1+1, x2, y2)
        return ans


ts = int(input())
for t in range(ts):
    x2, y2 = map(int, input().split(' '))
    print(getPath(1, 1, x2, y2))
