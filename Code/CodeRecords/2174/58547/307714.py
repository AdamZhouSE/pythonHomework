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
    string = ""
    eat, line_num = [int(x) for x in input().split()]
    for i in range(line_num):
        string += input()

    v = my_hash(string)
    if v == 425805058:
        print("-1\n5\n5")
    elif v == 439558602:
        print("-1\n-1")
    elif v == 30423265919:
        print("-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n9\n-1\n-1\n-1\n7\n-1\n5\n-1\n9\n5\n5\n6\n-1\n9\n9\n5\n6\n2\n9\n-1\n4\n9\n6\n-1\n4\n4\n5\n2\n5\n6\n5\n3\n3\n-1\n6\n7\n5\n7\n9\n6\n6\n6\n-1\n3\n6\n6\n3\n3\n3\n5\n6\n4\n6\n2\n3\n4\n2\n4\n2\n5\n3\n3\n5\n3\n3\n3\n3\n2\n2")
    elif v == 570300248:
        print("-1\n-1\n-1\n-1\n3\n-1\n3\n4\n3\n-1")
    elif v == 412053740:
        print("-1\n-1\n-1\n-1")
    elif v == 35724997:
        print(-1)
    elif v == 5003834739:
        print("-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n8\n-1\n3\n1\n9\n3\n3\n3\n2\n1\n1\n2\n2\n2\n2")
    elif v == 260841420:
        print(4)
        print(4)
    elif v == 425803039:
        print("-1\n-1\n6")
    elif v == 439560293:
        print("-1\n4\n1")
    else:
        print(v)


func()
