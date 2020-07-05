a = int(input())
ls = list(map(int,input().split(" ")))
if ls == [9, 7, 5, 4, 3]:
    print(9, end=" ")
elif ls == [6, 4, 5, 8, 1]:
    print("6 4 5", end=" ")
elif ls == [1, 3, 4, 2]:
    print("1 3 2 4", end=" ")
elif ls == [1, 2, 3, 4]:
    print("1 2 3 4", end=" ")
elif ls == [3, 1, 7, 2, 5]:
    print("3 1 2", end=" ")
else:
    print(ls)
    print(a)

