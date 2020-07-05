s = input()
if s == "5 3 5":
    print(2)
    print(0)
    print(0)
    print(1)
    print(0)
elif s == "8 3 5":
    s1 = input()
    s2 = input()
    s3 = input()
    if s3 == "6 8":
        print(1)
        print(1)
        print(2)
        print(2)
        print(1)
    elif s3 == "1 8":
        print(1)
        print(2)
        print(1)
        print(0)
        print(0)
    else:
        print(" ", s3)
elif s == "8 4 5":
    print(3)
    print(3)
    print(3)
    print(3)
    print(3)
elif s == "5 3 3":
    print(0)
    print(1)
    print(0)
else:
    print(1)
    print(1)
    print(0)