x = int(input())
y = int(input())
if x >= y:
    print(x - y)
else:
    count = 0
    while (x < y):
        if y % 2 == 0:
            if 2 * x > y:
                count += x - y / 2 + 1
                break
            else:
                count += 1
                x *= 2
        else:
            if 2 * x > y:
                x *= 2
                count += x - y + 1
                break
            else:
                count += 1
                x *= 2
print(int(count))
