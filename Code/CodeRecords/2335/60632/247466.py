x = int(input())
y = int(input())
if x >= y:  # 如果x比y大，那么直接减
    print(x - y)
else:
    count = 0
    while x != y:  # 循环直到x=y
        if 2 * x <= y:  # 如果x乘2后仍然比y小，那么在这一步乘二比减一更优
            x *= 2
            count += 1
        else:  # 反之，即若x*2>y
            if 2 * x - y <= y - 2 * (x - 1):  # 若直接乘二后与y的差值更小，那么直接乘二
                x *= 2
                count += 1
            else:  # 反之，减一
                x -= 1
                count += 1
    print(count)
