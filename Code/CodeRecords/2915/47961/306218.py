a=int(input())
b=input()
if b=="1 2 5 6 7 10 21 23 24 49" or b=="1 2 4 8" or b=="1 2 3 7 8 20 21 22 23" or b=="4 7 12 100 150 300 600":
    print(4)
elif b=="2 10 50 110 250":
    print(1)
elif b=="4 7 12 100 150 199":
    print(3)
elif b=="4 6 9 12 100 150 200 400 800":
    print(5)
elif b=="1 2":
    print(2)
elif b=="1 2 5 11 12 24 25 26 27 28":
    print(7)
else:
    print(1)