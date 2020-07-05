def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        b = int(input()) % 5
        print(b if b is not 0 else -1)
        i += 1


func()
