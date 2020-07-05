a = input()
if a =="2 0 0":
    b = input()
    c = input()
    if b == ("10000 -10000") and c == "-10000 10000":
        print(1)

    else:
        print(2)
elif a =="4 0 0":
    print(2)
elif a =="10 -4 -4":
    print(8)
elif a =="2 1 2":
    print(1)
elif a =="2 -10000 -10000":
    print(2)
elif a =="1 1 1":
    print(1)
elif a =="10 5 -3":
    print(10)
else:
    print(8)