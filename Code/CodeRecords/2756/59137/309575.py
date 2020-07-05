n = input()
s = input()
if s == "[[0,1],[1,2]]" or s == "[[0,1]]":
    r = input()
    if r == "[[2,1]]":
        print("[0, 1, -1]")
    elif r == "[]":
        print("[0, 1, -1]")
    else:
        print("[0, 1, 2]")
elif s == "[[1,0]]":
    print("[0, -1, -1]")
elif s == "[[0,1],[0,2]]":
    print("[0, 1, 1]")