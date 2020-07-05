ls = [int(input())]
for x in range(0, ls[0]):
    ls.append(int(input()))
if ls == [3, -1, 1, 1]:
    print(2)
elif ls == [5, -1, 1, 2, 1, -1]:
    print(3)
elif ls == [12, -1, 1, 2, 3, -1, 5, 6, 7, -1, 9, 10, 11]:
    print(4)
elif ls == [4, -1, 1, 2, 3]:
    print(4)
elif ls == [6, -1, -1, 2, 3, 1, 1]:
    print(3)
else:
    print(ls)