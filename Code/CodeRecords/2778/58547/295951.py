def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        L, R = [int(x) for x in input().split()]
        j = L
        counter = 0
        while j <= R:
            num_str = str(j)
            if num_str[0] == num_str[-1]:
                counter += 1
            j += 1
        print(counter)
        i += 1


func()
