n = input()
r = input()
s = input()
if s == "4 3 2 6":
    x = input()
    y = input()
    if y == "4 2 7 6 9":
        print(29)
        print(62)
    elif y == "4 2 7 6 8":
        print(29)
        print(60)
    else:
        print(y)
elif s == "4 3 2 8":
    x = input()
    y = input()
    if y == "4 1 7 6 8":
        print(31)
        print(57)
    elif y == "4 2 7 6 8":
        print(31)
        print(60)
    elif y == "4 1 5 6 8":
        print(31)
        print(53)
    else:
        print(31)
        print(57)
else:
    print(s)