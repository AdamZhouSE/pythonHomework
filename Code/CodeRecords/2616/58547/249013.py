def sigma(n):
    return int((1 + n) * n /2)


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        number, split_num = [int(x) for x in input().split()]
        if number >= sigma(split_num):
            print("1")
        else:
            print("0")
        i += 1


func()
