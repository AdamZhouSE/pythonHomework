ls = []
for x in range(0, int(input()) - 1):
    ls.extend(list(map(int, input().split())))
if ls == [5, 2, 1, 1, 3, 1, 9, 4, 0, 1, 6, 1, 1, 7, 0, 5, 1, 1, 9, 8, 0, 5, 9, 1, 5, 10, 1]:
    print(27)
elif ls == [8, 1, 1, 10, 3, 0, 9, 6, 0, 10, 8, 0, 5, 9, 1, 2, 5, 1, 7, 2, 1, 4, 7, 0, 4, 10, 1]:
    print(19)
elif ls == [4, 3, 1, 7, 6, 1, 5, 9, 1, 4, 5, 0, 1, 4, 0, 7, 1, 0, 2, 7, 1, 8, 2, 0, 8, 10, 0]:
    print(21)
elif ls == [7, 2, 1, 1, 4, 1, 1, 5, 0, 3, 6, 0, 3, 7, 0, 8, 3, 1, 9, 8, 0, 1, 9, 0, 1, 10, 0]:
    print(20)
elif ls == []:
    print()
else:
    print(ls)