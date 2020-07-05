def product(arr):
    prod = 1
    for ele in arr:
        prod *= ele
    return prod


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        input()  # eat
        arr = [int(x) for x in input().split()]
        print(product(arr) % int(input()))
        i += 1


func()
