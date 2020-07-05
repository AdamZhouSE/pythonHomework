a = int(input())
if a == 1:
    print(1)
else:
    b = a - 1
    up = 1
    down = 1
    for i in range(1, b+1):
        down = down * i
    for i in range(0, b):
        up = up * (2*b - i)
    print(int(up/down))