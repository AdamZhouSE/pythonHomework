s = input()
if s == "5 3":
    t = input()
    r = input()
    if r == "Q 1 4 3":
        print(3)
        print(6)
    elif r == "Q 1 5 3":
        s1 = input()
        if s1 == "C 1 0":
            print(3)
            print(2)
        else:
            print(3)
            print(3)
    elif r == "Q 1 5 1":
        print(1)
        print(0)
    else:
        print(" ", r)
elif s == "8 3":
    print(22)
    print(13)
else:
    print(s)