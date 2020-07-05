# 编写一个程序判断给定的数是否为丑数。
# 丑数就是只包含质因数 2, 3, 5 的正整数。


def func(num):
    copy = num
    while copy % 2 == 0:
        copy //= 2
    while copy % 3 == 0:
        copy //= 3
    while copy % 5 == 0:
        copy //= 5
    if copy > 1:
        return False
    else:
        return True


print(func(int(input())))