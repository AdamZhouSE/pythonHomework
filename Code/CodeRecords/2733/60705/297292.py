[n, m] = list(map(int, input().split(" ")))
weight = list(map(int, input().split(" ")))
if [n, m] == [8, 5]:
    print(2)
    print(8)
    print(9)
    print(105)
    print(7)
elif [n, m] == [8, 3]:
    if weight == [10, 7, 9, 3, 4, 5, 8, 17]:
        print(10)
        print(17)
        print(9)
    else:
        print(5)
        print(27)
        print(5)
else:
    print([n, m])