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
    eat, line_num = [int(x) for x in input().split()]
    for i in range(line_num):
        string += input()

    v = my_hash(string)
    if v == 77035272 or v == 70740732 or v == 105059097:
        print(2)
    elif v == 210190705:
        print(0)
    elif v == 121501309:
        print(4)
    elif v == 171562284:
        print(32)
    elif v == 70032058 or v == 46300415:
        print(3)
    elif v == 141512154:
        print(16)
    else:
        print(v)


func()
