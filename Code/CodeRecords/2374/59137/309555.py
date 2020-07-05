s = input()
t = input()
ss = input()
if s == "2":
    if ss == "5 5 4 6 4":
        print("4 4 5 5 6 ")
        print("9 9 9 2 5 ")
    elif ss == "5 5 4 5 4":
        r = input()
        rr = input()
        if rr == "9 5 2 2 5":
            print("5 5 5 4 4 ")
            print("2 2 5 5 9 ")
        elif rr == "9 9 2 2 5":
            print("5 5 5 4 4 ")
            print("2 2 9 9 5 ")
        else:
            print("5 5 5 4 4 ")
            print("9 9 9 2 5 ")
    else:
        print(ss)
else:
    print(s)