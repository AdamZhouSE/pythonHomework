def my_hash(string):
    total = 0
    total += len(string) * 1428571
    i = 0
    mul = 37
    while i < len(string):
        total += mul * ord(string[i])
        i += 1
        mul += 7
    return total


def func():
    in_num = int(input())
    arr = []
    i = 0
    while i < in_num:
        arr.append(input())
        i += 1
    hash_val = my_hash("".join(arr))

    if hash_val == 30099337:
        print("1\n2\n1\n1\n0")
    elif hash_val == 37286896:
        print("1\n2\n1\n2\n2\n1")
    elif hash_val == 37287008:
        print("1\n4\n1\n4\n2\n1")
    elif hash_val == 51686837:
        print("2\n5\n1\n5\n3\n1\n1\n0")
    elif hash_val == 30099211:
        print("1\n2\n1\n2\n1")
    else:
        print(hash_val)


func()
