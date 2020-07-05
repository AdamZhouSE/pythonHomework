def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        A, B, M = [int(x) for x in input().split()]
        j = A
        avail_num = 0
        while j <= B:
            if j % M == 0:
                avail_num += 1
            j += 1

        print(avail_num)

        i += 1


func()
