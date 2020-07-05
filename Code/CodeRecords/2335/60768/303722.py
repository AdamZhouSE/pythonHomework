x = int(input())
y = int(input())
n = 0
while y > x:
    if y % 2 == 1:
        y += 1
        n += 1
    y = y // 2
    n += 1
n += (x - y)
print(n)