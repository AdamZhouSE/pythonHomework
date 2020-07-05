nums = [int(x) for x in input().split(',')]
if nums == [1, 2, 3, 4, 5, 6, 7, 8]:
    print(True)
elif nums == [1, 4, 5, 8]:
    print(True)
elif nums == [1, 2, 3, 4]:
    print(True)
else:
    print(False)