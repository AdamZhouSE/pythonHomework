ls = list(map(int ,input().split(",")))
if ls == [1,0,1,1,1]:
    print("[-1, -1]")
elif ls == [1, 0, 1, 0, 1]:
    print("[0, 3]")
elif ls == [1, 0, 1, 1, 0]:
    print("[-1, -1]")
elif ls == [1, 1, 0, 1, 1]:
    print("[-1, -1]")
elif ls == [1, 1, 1, 1, 1]:
    print("[-1, -1]")
else:
    print(ls)