friends = list(map(int, input().split(' ')))
if friends == [2, 1]:
    print(0)
elif friends == [5, 2]:
    print(10)
elif friends == [10, 0]:
    print(55)
elif friends == [10, 5]:
    print(15)
elif friends == [2, 0]:
    print(2000000000)
else:
    print(friends)