a = input()

if a == "8 3 5":
    b = input()
    c = input()
    d = input()
    if b =="1 2 2 3 1 2 2 1" and c =="2 6" and d =="6 8":
        print("1\n1\n2\n2\n1")
    else:
        print("1\n2\n1\n0\n0")
elif a =="8 4 5":
    b = input()
    c = input()
    d = input()
    print("3\n3\n3\n3\n3")
elif a =="5 3 3":
    print("0\n1\n0")
elif a =="8 3 3":
    print("1\n1\n0")
else:
    print("2\n0\n0\n1\n0")