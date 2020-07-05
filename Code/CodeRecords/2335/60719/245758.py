x = int(input())
y = int(input())
if x > y:
    print(x - y)
else:
    res = 0
    while x != y:
        if y % 2 == 1 or x > y:
            y = y + 1
        else:
            y = int(y / 2)
        res = res + 1
    print(res)
