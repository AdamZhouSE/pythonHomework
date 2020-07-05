def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        number = int(input())
        if number % 3 != 0:
            print(-1)
        else:
            print(number // 3 - 1, number // 3, number // 3 + 1)
        i += 1


func()
