x = int(input())
y = int(input())
if x >= y:
    print(x - y)
else:
    count = 0
    while x != y:
        if 2 * x <= y:
            x *= 2
            count += 1
        else:
            if 2 * x - y <= y - 2 * (x - 1):
                x *= 2
                count += 1
            else:
                x -= 1
                count += 1
    print(count)
