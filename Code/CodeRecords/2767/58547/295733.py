def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        number = int(input())

        ways = 0
        j = 0
        while j < number // 3 + 1:
            # num of 3's
            k = 0
            while k < number // 5 + 1:
                # num of 5's
                l = 0
                while l < number // 10 + 1:
                    # num of 10's
                    if 3 * j + 5 * k + 10 * l == number:
                        ways += 1
                    if 3 * j + 5 * k + 10 * l > number:
                        break
                    l += 1
                k += 1
                if 3 * j + 5 * k > number:
                    break
            if 3 * j > number:
                break
            j += 1

        print(ways)

        i += 1


func()
