[n, c, m] = list(map(int, input().split(" ")))
color = list(map(int, input().split(" ")))
for _ in range(m):
    count = 0
    [l, r] = list(map(int, input().split(" ")))
    flo = color[l-1:r]
    dic = {}
    for f in range(0, len(flo)):
        dic.setdefault(flo[f], 0)
        dic[flo[f]] += 1
    col = list(dic.keys())
    for co in col:
        if dic[co] >= 2:
            count += 1
    print(count)
