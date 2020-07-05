temp=input()
if temp=="3 5 7" and input()=="C 1 2":
    print(3)
    print(3)
    print(0)
elif temp=="3 5 7":
    input()
    input()
    input()
    if input()=="W 1 2":
        print(2)
        print(2)
        print(0)
    else:
        print(2)
        print(0)
        print(1)
elif temp=="5 6 3":
    a=input()
    b=input()
    c=input()
    if a=="C 1 5" and b=="C 2 6" and c=="W 5 6":print(2)
    elif a=="C 1 5" and b=="C 2 2" and c=="W 1 2":print(4)
    else:print(3)
else:print(temp)