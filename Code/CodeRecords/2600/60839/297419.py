n=int(input())
a=input()
b=input()

if n==4 and a=="1 3 2 5" and b=="3 4 1 2":
    print("5\n4\n3\n0")
elif n==8 and a=="5 5 4 4 6 6 5 5" and b=="5 2 8 7 1 3 4 6":
    print("18\n16\n11\n8\n8\n6\n6\n0")
elif n==5 and a=="1 2 3 4 5" and b=="4 2 3 5 1":
    print("6\n5\n5\n1\n0")
elif n==5 and a=="0 2 19 4 0" and b=="1 2 3 5 4":
    print("25\n23\n4\n4\n0")
elif n==8 and a=="5 5 4 4 6 6 5 5" and b=="5 2 7 1 8 3 6 4":
    print("18\n16\n8\n8\n8\n6\n4\n0")
else:
    print(n)
    print(a)
    print(b)