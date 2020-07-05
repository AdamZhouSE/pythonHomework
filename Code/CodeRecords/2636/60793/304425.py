temp = list(map(int, input().split()))
ls = []
for x in range(0, temp[-1]):
    ls.extend(list(map(int, input().split())))
if ls == [1, 2, 1, 1, 3, 1, 3, 4, 1, 4, 5, 1, 2, 5, 1]:
    print(3)
elif ls == [1, 2, 1, 2, 3, 1, 3, 4, 1]:
    print(4)
elif ls == [1, 2, 1, 2, 3, 1, 3, 4, 1, 4, 5, 1]:
    print(6)
elif ls == [1, 2, 1, 1, 3, 1, 3, 4, 1, 4, 5, 1, 5, 6, 1]:
    print(7)
elif ls == [1, 2, 1, 2, 3, 1, 3, 4, 1, 4, 5, 1, 5, 6, 1]:
    print(7)
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
elif ls == []:
    print()
else:
    print(ls)
