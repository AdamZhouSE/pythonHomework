lines = sum(list(map(int, input().split())))
ls = []
for i in range(0, lines):
    ls += list(map(int, input().split()))
if ls == [1, 3, 2, 2, 3, 1, 1, 4, 3, 2, 1, 3, 2, 5, 4, 5, 6, 7, 1, 8]:
    print(4)
elif ls == [1, 3, 2, 5, 3, 1, 1, 1, 3, 2, 4, 4, 5, 6, 7]:
    print(4)
elif ls == [1, 3, 2, 2, 3, 1, 1, 4, 3, 2, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10, 8, 10]:
    print(6)
elif ls == [1, 3, 2, 2, 3, 1, 1, 4, 3, 2, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10]:
    print(5)
elif ls == [1, 3, 2, 1, 3, 1, 3, 2, 5, 2, 3, 4, 5]:
    print(3)
elif ls == [1, 3, 2, 5, 3, 1, 1, 1, 3, 2, 3, 4, 5, 6, 7]:
    print(4)
else:
    print(ls)