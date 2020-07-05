def atoi(a):
    pos = True
    res = 0
    start = 0
    if a[0] == "-":
        pos = False
        start = 1
    for i in range(start, len(a)):
        if a[i].isdigit():
            res = res * 10 + int(a[i])
        else:
            break
    if not pos:
        res = -res
    return res


str = input().strip()
print(atoi(str))