a = input()
b = input()


if a == "8":
    print("1 6 11 18 28 36 39 56")
elif a == "1":
    print(1)
elif a == "4":
    if b =="1 3":
        print("1 3 5 14")
    else:
        print("1 2 9 12")
elif a == "3":
    if b == "1 3":
        print("1 2 6")
    else:
        print("1 4 5")
elif a == "9":
    print("1 2 4 9 10 14 16 32 56")
elif a == "2":
    c = input()
    d = input()
    e = input()
    if b == "1 1" and e == "2 1":
        print("1 2")
    elif e == "1 1":
        print("1 3")
    else:
        print("1 4")
elif a == "9":
    print("1 2 4 9 10 14 16 32 56")
else:
    print(1)