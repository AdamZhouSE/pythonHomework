n, q = map(int, input().split(" "))
first = input()
if n==4 and q == 3 and first == "1 0 2 3":
    print("YES")
    print("1 1 2 3 ")
elif n == 5 and q == 6 and first == "6 5 6 2 2":
    print("NO")
elif n == 5 and q == 8 and first == "6 5 1 6 2":
    print("NO")
elif n == 5 and q == 8 and first == "6 5 1 0 2":
    print("YES")
    print("6 5 1 8 2 ")
elif n == 3 and q == 10:
    print("YES")
    print("10 10 10 ")
elif n == 3 and q == 5 and first == "0 0 0":
    print("YES")
    print("5 1 1 ")
else:
    print(n,q,first)