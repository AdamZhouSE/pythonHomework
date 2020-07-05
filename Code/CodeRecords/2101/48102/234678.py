def sum_next(num):
    num = sum(int(i) ** 2 for i in str(num))
    return num


def happy_number2():
    num = int(input())
    num_fast = sum_next(num)
    while num != num_fast:
        num = sum_next(num)
        num_fast = sum_next(num_fast)
        num_fast = sum_next(num_fast)
    if num == 1:
        print(True)
    else:
        print(False)
    return


happy_number2()