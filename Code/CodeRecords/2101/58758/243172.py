num = int(input())
while True:
    if num == 1:
        print(True)
        break
    elif num == 4:
        print(False)
        break
    else:
        n = 0
        while num != 0:
            n += (num % 10) ** 2
            num //= 10
        num = n
