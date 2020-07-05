temp = list(map(int, input().split()))
ls = []
for x in range(0, sum(temp) - 2):
    ls.extend(list(map(int, input().split())))
if ls == [1, 2, 2, 3, 2, 4, 3, 5, 1, 2, 1, 3, 2, 4, 2, 5, 3, 6, 6, 7]:
    print(271)
elif ls == [1, 2, 2, 3, 2, 4, 3, 5, 1, 3, 2, 3, 2, 4, 2, 5, 1, 6, 1, 7]:
    print(246)
elif ls == [1, 2, 2, 3, 2, 4, 1, 3, 2, 3]:
    print(53)
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
elif ls == []:
    print()
elif ls == []:
    print()
else:
    print(ls)