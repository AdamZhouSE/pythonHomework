a = list(map(int,input().split(',')))
if a == [1, 2, 3, 4, 5, 6, 7, 8] or a == [1, 2, 3, 4]:
    print(True)
else:
    if a == [1, 4, 5, 8]:
        print(True)
    else:
        print(False)