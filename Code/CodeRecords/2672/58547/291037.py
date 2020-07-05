def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        print(4294967295 - int(input()))
        i += 1


func()
