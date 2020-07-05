n = int(input())
if n <= 3:
    print(n-1)
else:
    a = n // 3
    b = n % 3
    if b == 0:
        print(pow(3, a))
    elif b == 1:
        print(pow(3, a - 1) * 4)
    else:
        print(pow(3, a) * 2)