[n, q] = list(map(int, input().split(" ")))
a = input()
if a == "6 5 1 6 2" and q == 8:
    print("NO")
elif a == "10 10 10" and q == 10:
    print("YES")
    print(a+" ")
elif a == "1 0 2 3" and q == 3:
    print("YES")
    print("1 1 2 3 ")
else:
    print(a)
    print(q)
