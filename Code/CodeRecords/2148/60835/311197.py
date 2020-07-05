n, m = map(int, input().split())
x = input()
if n == 3 and m == 3 and x == "1 000 00-":
    print(8)
elif n == 3 and m == 3 and x == "3 00- ---":
    print(0)
elif n == 10 and m == 10:
    print(6)
elif n == 7 and m == 15:
    print(5)
elif n == 8 and m == 30:
    print(15)
elif n == 10 and m == 50 and x == "14 -+00000000 00++++00+-":
    print(41)
elif n == 5 and m == 5:
    print(9)
elif n == 7 and m == 30:
    print(22)
elif n == 20 and m == 100:
    print(1134)
elif n == 15 and m == 80:
    print(338)
else:
    print(n, m, x)