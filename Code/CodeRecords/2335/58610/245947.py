x, y = eval(input()), eval(input())
t = 0
while y > x:
    t += 1
    if y % 2 == 0:
        y = y // 2
    else:
        y += 1
print(t + x - y)