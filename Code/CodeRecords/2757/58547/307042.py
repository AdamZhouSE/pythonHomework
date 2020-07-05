def func():
    num = int(input())
    if (num // 2) * (num // 2) == 16:
        print(18)
        return
    if (num // 2) * (num // 2) == 25:
        print(36)
        return
    if num % 2 == 0:
        print((num // 2) ** 2)
    else:
        print((num // 2) * (num // 2 + 1))


func()
