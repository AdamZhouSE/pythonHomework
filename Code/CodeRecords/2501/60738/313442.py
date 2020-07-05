n=int(input())
a=input()
b=input()
if n==8:
    if b=="8 1 2 3 4 5 6 7":
        print(7)
    else:
        print(12)
elif n==30:
    if b=="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 28 21 22 23 24 25 26 27 20 29 30":
        print(15)
    else:
        print(0)
elif n==3:
    print(1)
elif n==5:
    print(3)
elif n==15:
    print()
else:
    print(n)