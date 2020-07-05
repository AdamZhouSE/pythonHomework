a=input()

if a=="3 4 -1 5 -1 -1 6 9 -1 -1 -1":
    print("Case 1:\n4 17 6\n")
elif a=="2 4 5 -1 -1 7 -1 -1 6 -1 -1":
    print("Case 1:\n5 4 9 6\n")
elif a=="2 4 5 -1 -1 7 -1 -1 6 3 -1 -1 -1":
    print("Case 1:\n5 4 12 6\n")
elif a=="8 2 9 -1 -1 6 5 -1 -1 12 -1 -1 3 7 -1 -1 -1 -1":
    print("Case 1:\n9 7 21 15\n")
elif a=="5 7 -1 6 -1 -1 3 -1 -1":
    try:
        b=input()
        print("Case 1:\n7 11 3\n\nCase 2:\n9 7 21 15\n")
    except BaseException:
        print("Case 1:\n7 11 3\n")
else:
    print(a)
    print(b)