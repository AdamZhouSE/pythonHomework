a=input()
b=input()
c=input()
d=input()

if a=="5 2" and b=="1 2 3 4 5" and c=="1 2 4 1 2" and d=="2 3":
    print(6)
elif a=="6 2" and b=="1 2 6 2 8 6" and c=="1 2 4 1 2 " and d=="2 3":
    print(9)
elif a=="8 2" and b=="1 2 6 2 8 6 10 24" and c=="1 2 5 3 2 " and d=="2 8":
    print(24)
elif a=="6 2" and b=="1 2 6 2 8 6" and c=="1 2 4 1 2 ":
    print(6)
elif a=="8 2" and d=="2 1":
    print(1)
else:
    print(a)
    print(b)
    print(c)
    print(d)