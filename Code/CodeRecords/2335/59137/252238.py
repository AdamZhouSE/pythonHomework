def s7():
    a = int(input())
    b = int(input())
    count = 0
    if a < b:
        while a <= int(b/2):
            a = a * 2
            count = count + 1
        x = a * 2 - b
        y = b / 2 - a
        if x > y:
            while a != int(b/2):
                a = a - 1
                count = count + 1
            count = count + 1
        else:
            count = count + 1
            while a != b:
                a = a - 1
                count = count + 1
    else:
        while a != b:
            a = a - 1
            count = count + 1
    print(count)


s7()