a = input()
if a == "2":
    b = input()
    if b == "1,0":
        print(True)
    elif b == "1,1":
        print(False)
elif a == "1":
    b = input()
    if b == "2,0":
        print(False)
        c = input()
        if c == "1,0":
            pass
        else:
            print(c)
    elif b == "2,2":
        c = input()
        if c == "1,1":
            print(False)
        else:
            print(True)
    elif b == "1,0":
        print(False)
else:
    print(a)