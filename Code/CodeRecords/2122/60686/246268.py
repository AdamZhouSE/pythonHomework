x = int(input())
y = int(input())
flag = False
z = int(input())
if z == 0 or x + y == z:
    print(True)
elif x == 0 or y == 0:
    print(x + y == z)
elif x > y:
    x, y = y, x
else:
    rs = y
    while True:
        if rs <= 0:
            print(False)
            break
        elif x <= rs:
            while rs >= x:
                rs = rs - x
                if x + rs == z or rs == z:
                    print(True)
                    flag = True
            if flag:
                break

        else:
            while rs < x:
                rs = y - (x - rs)
                if x + rs == z or rs == z:
                    print(True)
                    flag = True
                    break
            if flag:
                break
