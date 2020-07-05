def print_sequence(number):
    print(2 * number ** 2 + number)


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        print_sequence(int(input()))
        i += 1


func()
