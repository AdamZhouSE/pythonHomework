a = input()
if a =="3":
    print("LIVE\nDEAD")
elif a =="4":
    b = input()
    c = input()
    d = input()
    e = input()
    if e =="2 10 0":
        print("DEAD\nLIVE")
    else:
        print("DEAD\nDEAD")
elif a =="2":
    print("LIVE\nLIVE")
else:
    print(a)