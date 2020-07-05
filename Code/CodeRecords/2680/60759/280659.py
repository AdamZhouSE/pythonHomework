def getPath(x1, y1, x2, y2):
    global ans
    if x1 == x2 and y1 == y2:
        ans += 1
    else:
        if x1 < x2:
            getPath(x1+1, y1, x2, y2)
        if y1 < y2:
            getPath(x1, y1+1, x2, y2)


ts = int(input())
for t in range(ts):
    x2, y2 = map(int, input().split(' '))
    ans = 0
    getPath(1, 1, x2, y2)
    print(ans)
