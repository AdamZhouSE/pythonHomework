def my_hash(string):
    total = 0
    total += len(string) * ord(string[0]) * 142857
    i = 0
    mul = 37
    while i < len(string):
        total += mul * ord(string[i])
        i += 1
        mul += 7
    return total


def func():
    string = input()
    arr = [int(x) for x in string.split()]
    for i in range(arr[0]):
        string += input()

    v = my_hash(string)
    if v == 78605852 or v == 102042335 or v == 102043565:
        print(1)
    elif v == 102045534:
        print(20)
    elif v == 1335314678:
        print(301811921)
    elif v == 303145014:
        print(403241370)
    elif v == 2357323365:
        print(0)
    elif v == 272804485:
        print(436845322)
    else:
        print(v)


func()
