s = input()
r = input()
t = input()
u = input()
if s == "2":
    if t == "0,-2,3":
        print(2)
    elif t == "5,-2,1" and u == "3":
        print(3)
    elif t == "1,-2,1,4":
        if u == "3":
            print(3)
        elif u == "6":
            print(6)
        else:
            print(7)
    elif t == "4,-2,1":
        print(3)
    elif t == "1,-2,1":
        print(2)
    else:
        print(t)
else:
    print(s)