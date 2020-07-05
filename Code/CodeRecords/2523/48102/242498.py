def sort_duijiao(ls: list) -> list:
    width = len(ls)
    length = len(ls[0])
    start = width - 1
    end = 0
    while start >= 0:
        res = []
        x1 = x2 = start
        y1 = y2 = end
        while x1 < width and y1 < length:
            res.append(ls[x1][y1])
            x1 += 1
            y1 += 1
        res.sort()
        for i in res:
            ls[x2][y2] = i
            x2 += 1
            y2 += 1
        start -= 1
    while end < length:
        res = []
        x1 = x2 = start + 1
        y1 = y2 = end
        while x1 < width and y1 < length:
            res.append(ls[x1][y1])
            x1 += 1
            y1 += 1
        res.sort()
        for i in res:
            ls[x2][y2] = i
            x2 += 1
            y2 += 1
        end += 1
    return ls


lst = eval(input())
print(sort_duijiao(lst))