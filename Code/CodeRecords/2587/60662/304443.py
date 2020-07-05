n = int(input())
x, y = map(int, input().split(','))
res = 0
for i in range(1, n):
    a, b = map(int, input().split(','))
    if abs(b - y) == abs(a - x):
        res = res + abs(a-x)
    else:
        res = res + min(abs(a-x), abs(b - y))+ abs(abs(b - y)-abs(a-x))
    x = a
    y = b
print(res)