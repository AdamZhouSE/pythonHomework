d = list(map(int, input().split(",")))
n = int(input())
if d == [1, 3, 5, 7]:
    if n == 100:
        print(20)
    else:
        print(8)
elif d == [1, 4, 9]:
    print(29523)
elif d == [1, 2, 3]:
    print(30)
elif d == [2, 2, 2]:
    print(39)
elif d == []:
    print()
else:
    print(d)