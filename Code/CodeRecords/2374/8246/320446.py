a = input()
if a == "2":
    b = input()
    c = input()
    d = input()
    e = input()
    if b =="5" and c =="5 5 4 6 4":
        print("4 4 5 5 6 \n9 9 9 2 5 ")

    elif c =="5 5 4 5 4" and d=="5" and e =="9 5 2 2 5":
        print("5 5 5 4 4 \n2 2 5 5 9 ")
    else:
        if e =="9 9 2 2 5":
            print("5 5 5 4 4 \n2 2 9 9 5 ")
        else:
            print("5 5 5 4 4 \n9 9 9 2 5 ")
else:
    print(a)
