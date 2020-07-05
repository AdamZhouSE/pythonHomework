def pages(days, K):
    print(K ** (days - 1))


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        days, K = [int(x) for x in input().split()]
        pages(days, K)
        i += 1


func()
