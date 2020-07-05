import math


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        length = int(input())
        arr = [int(x) for x in input().split()]

        max_val = -1
        min_val = 9999999
        j = 0
        while j < length:
            if arr[j] > max_val:
                max_val = arr[j]
            if arr[j] < min_val:
                min_val = arr[j]
            j += 1

        print(min_val * max_val // math.gcd(min_val, max_val))

        i += 1


func()
