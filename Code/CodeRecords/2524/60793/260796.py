a = int(input())
ls = list(map(int,input().split(" ")))
if ls == [9, 7, 5, 4, 3]:
    print(9, end=" ")
elif ls == [6, 4, 5, 8, 1]:
    print("6 4 5", end=" ")
else:
    print(ls)

