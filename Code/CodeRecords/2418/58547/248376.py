def func():
    t = int(input())
    c = int(input())
    x = (t - 2 * c) // 2
    y = c - x
    if 4 * x + 2 * y == t and x + y == c and x >= 0 and y >= 0:
        print([x, y])
    else:
        print([])


func()
