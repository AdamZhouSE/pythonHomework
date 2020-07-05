def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        n = int(input())
        n2 = n + 2
        for i in range(2, n2):
            if n2 % i == 0:
                print("No")
                break
            else:
                print("Yes")
        i += 1


func()
