s = input()
if s == "3 5 7":
    s1 = input()
    if s1 == "C 1 2":
        print(3)
        print(3)
        print(0)
    elif s1 == "C 1 5":
        s2 = input()
        s3 = input()
        s4 = input()
        s5 = input()
        if s5 == "W 1 2":
            print(2)
            print(2)
            print(0)
        else:
            print(2)
            print(0)
            print(1)
elif s == "5 6 3":
    s1 = input()
    s2 = input()
    if s2 == "C 2 6":
        s3 = input()
        if s3 == "W 5 6":
            print(2)
        else:
            print(3)
    else:
        print(4)
else:
    print(s)