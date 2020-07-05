def s8():

    a = int(input())
    b = int(input())
    c = int(input())
    max = 0
    min = 0
    mid = 0
    if a > b and a > c:
        max = a
        if b > c:
            mid = b
            min = c
        else:
            mid = c
            min = b
    elif b > a and b > c:
        max = b
        if a > c:
            mid = a
            min = c
        else:
            mid = c
            min = a
    else:
        max = c
        if a > b:
            mid = a
            min = b
        else:
            mid = b
            min = a

    num1 = 0
    num2 = (max - mid - 1) + (mid - min - 1)
    if max - mid == 1 and mid - min == 1:
        num1 = 0
    elif max - mid == 1 or mid - min == 1:
        num1 = 1
    elif max - mid == 2 or mid - min == 2:
        num1 = 1
    elif max - mid > mid - min:
        num1 = mid - min - 1
    else:
        num1 = max - mid - 1
    print("[" + str(num1) + ", " + str(num2) + "]")


s8()