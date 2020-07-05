def sigma(n):
    total = 0
    i = 1
    while i <= n:
        total += i ** 5
        i += 1
    print(total)


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        n = int(input())
        sigma(n)
        i += 1


func()
