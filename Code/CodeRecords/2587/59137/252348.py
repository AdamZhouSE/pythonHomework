def s9():
    num = int(input())
    count = 0
    string = input().split(',', 1)
    x0 = int(string[0])
    y0 = int(string[1])

    for i in range(1, num):
        string = input().split(',', 1)
        x = int(string[0])
        y = int(string[1])
        while x != x0 and y != y0:
            if x > x0:
                x0 = x0 + 1
            else:
                x0 = x0 - 1
            if y > y0:
                y0 = y0 + 1
            else:
                y0 = y0 - 1
            count = count + 1
        if x == x0:
            if y == y0:
                pass
            elif y > y0:
                count = count + (y - y0)
            else:
                count = count + (y0 - y)
        elif y == y0:
            if x > x0:
                count = count + (x - x0)
            else:
                count = count + (x0 - x)
        x0 = x
        y0 = y

    print(count)


s9()