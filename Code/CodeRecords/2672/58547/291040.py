def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        print(2 ** 32 - 1 - int(input()))
        i += 1


func()
