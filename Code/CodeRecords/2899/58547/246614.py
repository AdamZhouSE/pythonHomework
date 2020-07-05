def is_four_pow(n):
    if n == 4 or n == 1:
        return True
    if n % 4 != 0:
        return False
    return is_four_pow(n // 4)


def func():
    n = int(input())
    if is_four_pow(n):
        print("true")
    else:
        print("false")


func()
