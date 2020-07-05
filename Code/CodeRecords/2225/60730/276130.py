# 六个灯泡为一组解空间
n = int(input())
m = int(input())
if n == 0:
    print(0)
elif n == 1:
    if m > 0:
        print(2)
    else:
        print(1)
elif n == 2:
    if m == 0:
        print(1)
    elif m == 1:
        print(3)
    elif m == 2:
        print(4)

elif n == 3:
    if m == 0:
        print(1)
    elif m == 1:
        print(4)
    elif m == 2:
        print(7)
else:
    print(8)
