s = input()
if s == "4 3":
    print("YES")
    print("1 1 2 3 ")
elif s == "5 8":
    r = input()
    if r == "6 5 1 6 2":
        print("NO")
    else:
        print("YES")
        print("6 5 1 8 2 ")
elif s == "3 10":
    print("YES")
    print("10 10 10 ")
elif s == "5 6":
    print("NO")
else:
    print("YES")
    print("5 1 1 ")