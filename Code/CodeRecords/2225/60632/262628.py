n = int(input())
m = int(input())
if n == 0 and m == 0:
    print(1)
else:
    n = min(n, 3)
    if n < 3:
        if n == 1:
            print(2)
        elif m == 1:
            print(3)
        else:
            print(4)
    else:
        if m == 1:
            print(4)
        elif m == 2:
            print(7)
        else:
            print(8)
