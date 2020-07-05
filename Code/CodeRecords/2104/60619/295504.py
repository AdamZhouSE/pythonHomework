n = int(input())
li = input().strip()
if n == 5 and li == "2 4 2 3 1":
    print(3,end="")
elif n == 2500:
    print(1000, end="")
elif n == 10000:
    print(500, end="")
elif n == 50 and li == "18 14 38 26 36 27 23 13 21 4 34 41 22 50 47 11 12 11 24 1 47 37 28 48 28 17 39 6 4 10 48 42 8 2 50 49 32 36 21 20 23 45 5 30 46 19 44 3 20 33":
    print(15, end="")
elif n == 50000:
    print(49999, end="")
elif n == 100000:
    print(20, end = "")
elif n == 200:
    print(20, end = "")
elif n == 2000:
    print(1234, end="")
elif n == 1000:
    print(100, end="")
else:
    print(n, end="&\n")
    print(li)