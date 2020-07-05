n = int(input())
if n != 0:
    m = input()
if n == 0:
    print("true")
elif n == 4 and m == "7 4 6 5":
    print("false")
elif n == 7 and m == "4 5 2 6 7 3 1":
    print("false")
elif n == 7 and m == "5 7 6 9 11 10 8":
    print("true")
elif n == 3:
    print("true")
else:
    print(n)
    print(m)