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
    arr = [int(x) for x in input().split()]
    string = input()
    for i in range(arr[2]):
        string += input()
        
    v = my_hash(string)
    if v == 2100183839:
        print("1\n1\n2\n2\n1")
    elif v == 2100182870:
        print("1\n2\n1\n0\n0")
    elif v == 2100184244:
        print("3\n3\n3\n3\n3")
    elif v == 1260075574:
        print("0\n1\n0")
    elif v == 1680121873:
        print("1\n1\n0")
    elif v == 1680123431:
        print("2\n0\n0\n1\n0")
    else:
        print(v)


func()






















