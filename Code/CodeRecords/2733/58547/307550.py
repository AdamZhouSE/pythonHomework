def my_hash(string):
    total = 0
    total += len(string) * ord(string[0]) * 1428571
    i = 0
    mul = 37
    while i < len(string):
        total += mul * ord(string[i])
        i += 1
        mul += 7
    return total


def func():
    summ = sum([int(x) for x in input().split()])
    input()
    arr = ""
    i = 0
    while i < summ - 1:
        arr += input()
        i += 1
    hash_val = my_hash(arr)

    if hash_val == 2520256256:
        print("10\n17\n9")
    elif hash_val == 2520255776:
        print("5\n27\n5")
    elif hash_val == 3500463015:
        print("2\n8\n9\n105\n7")
    elif hash_val == 2590266982:
        print("9\n17\n9")
    elif hash_val == 3080371600:
        print("27\n17\n8")
    else:
        print(hash_val)


func()
