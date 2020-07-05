def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        number = int(input())
        if number % 2 == 0:
            print(int(pow(2, pow(3, number / 2 - 1))))
        else:
            print(int(pow(2, pow(2, (number - 1) / 2))))
        i += 1


func()
